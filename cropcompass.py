import simplejson as json
from flask import Flask, url_for, request, abort
import psycopg2
import logging

metadata_fields = ('name',
                   'description',
                   'table_name',
                   'unit',
                   'field',
                   'source_name',
                   'source_link')

table_fields = ('commodity','year','region')

# Checked later, and used to adjust WHERE clause for case insensitivity
lower_fields = ('commodity','region')


select_table_metadata = 'SELECT {METADATA_FIELDS} FROM metadata'.format(
                                      METADATA_FIELDS=','.join(metadata_fields))

select_data_template = """SELECT d.commodity,
                                 d.year,
                                 cl.region as region,
                                 d.{FIELD}
                                 FROM {TABLE_NAME} d
                                 LEFT JOIN region_lookup cl
                                 USING (fips)
                                 {WHERE_CLAUSE}
                                 ORDER BY (year,region, commodity) DESC
                                 {LIMIT_CLAUSE}
                                 {OFFSET_CLAUSE}
                                 """

class CropFlaskServer(Flask):
    def __init__(self, *args, **kwargs):
        super(CropFlaskServer, self).__init__(*args, **kwargs)
        self.dsn = "dbname=alex user=postgres port=55432 host=10.102.148.190 password=mysecretpassword"
        #self.dsn = "dbname=alex user=alex" # Testing DSN only
        self.conn = psycopg2.connect(self.dsn)

app = CropFlaskServer(__name__)

@app.route('/')
def root():
    link_template = ('CropCompass API - Make a GET request to '
                     '{URL} for a list of data sources')
    return link_template.format(URL=(request.url_root.rstrip('/')+
                                url_for('metadata_list_all')))
@app.route('/list')
def metadata_list_all():
    return make_json_response(metadata_lookup())

@app.route('/data/<table_name>')
def row_view(table_name):
    table_metadata = metadata_lookup(table_name)
    if not table_metadata:
        abort(404)
    row_keys = table_fields + (table_metadata['field'],)
    table_data = fetch_data(table_name, table_metadata)
    response = {'error':None,
                    'rows':len(table_data),
                    'data':dict_many(row_keys,table_data)}
    return make_json_response(response)

@app.route('/table/<table_name>')
def table_view(table_name):
    table_metadata = metadata_lookup(table_name)
    if not table_metadata:
        abort(404)
    row_keys = table_fields + (table_metadata['field'],)
    table_data = fetch_data(table_name, table_metadata)
    response = crop_dictionary(row_keys, table_metadata, table_data)
    return make_json_response(response)


def fetch_data(table_name, table_metadata):
    check_conn()
    with app.conn.cursor() as cur:
        where_clause, where_args = parse_where()
        limit, offset = parse_pagination()
        query = select_data_template.format(TABLE_NAME=table_name,
                                            FIELD=table_metadata['field'],
                                            WHERE_CLAUSE=where_clause,
                                            LIMIT_CLAUSE=' LIMIT %s',
                                            OFFSET_CLAUSE = ' OFFSET %s ')
#        logging.warning(cur.mogrify(query,where_args + [limit, offset]))
        cur.execute(query,where_args + [limit, offset])
        table_data = cur.fetchall()
    return table_data

def metadata_lookup(table_name=None):
    check_conn()
    with app.conn.cursor() as cur:
        if table_name:
            query = select_table_metadata + ' WHERE table_name = %s'
            cur.execute(query, (table_name,))
            row = cur.fetchone()
            if row:
                return dict_one(metadata_fields, row)
        else:
            cur.execute(select_table_metadata)
            metadata = []
            for row in cur:
                if row:
                    row_dict = dict_one(metadata_fields, row)
                    row_dict['row_view_url'] = (request.url_root.rstrip('/') +
                           url_for('row_view', table_name=row_dict['table_name']))
                    row_dict['table_view_url']  = (request.url_root.rstrip('/') +
                           url_for('table_view', table_name=row_dict['table_name']))
                    metadata.append(row_dict)
            return metadata
        return None

def check_conn():
    try:
        cur = app.conn.cursor()
        cur.execute('SELECT 1')
        cur.fetchall()
    except:
        app.conn = psycopg2.connect(app.dsn)

def make_json_response(data):
    resp = app.make_response(json.dumps(data))
    h = resp.headers
    h['Access-Control-Allow-Origin'] = '*'
    h['Content-Type'] = 'application/json'
    return resp

def crop_dictionary(row_keys, table_metadata, table_data):
    # Yes, this is not the prettiest code ever..
    # But at least it only iterates the resultset a single time to produce
    # the resulting table?

    crop_dict = {}
    field_name = table_metadata['field']
    for row in table_data:
        row_dict = dict_one(row_keys,row)
        if row_dict['commodity'] not in crop_dict:
            crop_dict[row_dict['commodity']] = []
        updated = False
        for record in crop_dict[row_dict['commodity']]:
            if record['year'] == row_dict['year']:
                if row_dict['region'] in record['regions']:
                    # This additional conditional stuff is ugly, but safeguards
                    # us from a bunch of null data in our datasets.
                    if row_dict[field_name]:
                        if record['regions'][row_dict['region']]:
                            # Checks that both sides are not Falsey
                            record['regions'][row_dict['region']] += row_dict[field_name]
                        else:
                            # If the right side is real, set the left side to it
                            record['regions'][row_dict['region']] = row_dict[field_name]
                        updated = True
                else:
                    record['regions'][row_dict['region']] = row_dict[field_name]
                    updated = True
        if not updated:
            # Needs a new record added for this year under this commodity
            new_record = {'year': row_dict['year'],
                          'unit': table_metadata['unit'],
                          'name': table_metadata['name'],
                          'regions': {
                            row_dict['region'] : row_dict[field_name]
                          }}
            crop_dict[row_dict['commodity']].append(new_record)
    return crop_dict


def parse_where():
    where_clause = []
    where_args = []
    for field in table_fields:
        field_param = request.args.get(field)
        if field_param:
            field_values = field_param.split(',')
            where_args.extend(field_values)
            if field in lower_fields:
                where_clause.append(('lower(' + field + ') in (%s)') %
                                    (','.join(['lower(%s)'] * len(field_values))))
            else:
                where_clause.append((field + ' in (%s)') %
                                (','.join(['%s'] * len(field_values))))
    if where_clause:
        return ('WHERE ' + ' AND '.join(where_clause), where_args)
    return ('',[])

def parse_pagination():
    limit = int(request.args.get('results',50))
    page = int(request.args.get('page', 1))
    # Basically keeps the minimum page at 1
    offset = (max(page, 1) - 1) * limit
    return limit, offset

def dict_one(keys, values):
    return dict(zip(keys,values))

def dict_many(keys, values):
    return [dict(zip(keys, row)) for row in values]

if __name__ == '__main__':
    app.run(debug=True)
