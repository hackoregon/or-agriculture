import simplejson as json
from flask import Flask, url_for, request
import psycopg2

metadata_fields = ('name',
                   'description',
                   'table_name',
                   'unit',
                   'field',
                   'source_name',
                   'source_link')

table_fields = ('crop','year','county')

select_table_metadata = 'SELECT {METADATA_FIELDS} FROM metadata'.format(
                                      METADATA_FIELDS=','.join(metadata_fields))

select_data_template = """SELECT d.crop,
                                 d.year,
                                 cl.county,
                                 d.{FIELD}
                                 FROM {TABLE_NAME} d
                                 LEFT JOIN county_lookup cl
                                 USING (fips)
                                 {WHERE_CLAUSE}
                                 {LIMIT_CLAUSE}"""

conn = psycopg2.connect("dbname=alex user=alex")

app = Flask(__name__)

@app.route('/')
def root():
    link_template = ('CropCompass API - Make a GET request to '
                     '{URL} for a list of data sources')
    return link_template.format(URL=(request.url_root.rstrip('/')+
                                url_for('metadata_list_all')))
@app.route('/list')
def metadata_list_all():
    return json.dumps(metadata_lookup())

@app.route('/data/<table_name>')
def data_table(table_name):
    table_metadata = metadata_lookup(table_name)
    row_keys = table_fields + (table_metadata['field'],)
    with conn.cursor() as cur:
        where_clause, where_args = parse_where()
        query = select_data_template.format(TABLE_NAME=table_name,
                                            FIELD=table_metadata['field'],
                                            WHERE_CLAUSE=where_clause,
                                            LIMIT_CLAUSE=' LIMIT 30')
        cur.execute(query,where_args)
        table_data = cur.fetchall()
    response = {'error':None,
                'rows':len(table_data),
                'data':dict_many(row_keys,table_data)}
    return json.dumps(response)

def metadata_lookup(table_name=None):
    with conn.cursor() as cur:
        if table_name:
            query = select_table_metadata + ' WHERE table_name = %s'
            cur.execute(query, (table_name,))
            row = cur.fetchone()
            return dict_one(metadata_fields, row)
        else:
            cur.execute(select_table_metadata)
            rows = cur.fetchall()
            metadata_dict = {}
            for row in rows:
                metadata = dict_one(metadata_fields,row)
                url = (request.url_root.rstrip('/') +
                       url_for('data_table', table_name=metadata['table_name']))

                metadata_dict[url] = metadata
            return metadata_dict

def parse_where():
    where_clause = []
    where_args = []
    for field in table_fields:
        field_param = request.args.get(field)
        if field_param:
            field_values = field_param.split(',')
            where_args.extend(field_values)
            where_clause.append((field + ' in (%s)') %
                                (','.join(['%s'] * len(field_values))))
    if where_clause:
        return ('WHERE ' + ' AND '.join(where_clause),
                where_args)
    return ('',[])


def dict_one(keys, values):
    return dict(zip(keys,values))

def dict_many(keys, values):
    return [dict(zip(keys, row)) for row in values]

if __name__ == '__main__':
    app.run(debug=True)
