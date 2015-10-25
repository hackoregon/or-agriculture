import cropcompass as db
import pandas




def _get_data(table_name):
    table_metadata = db.metadata_lookup(table_name)
    if not table_metadata:
        abort(404)
    row_keys = db.table_fields + (table_metadata['field'],)
    table_data = db.fetch_data(table_name, table_metadata)
    return row_keys, table_data


def test():
    data = [
            {'season': 5, 'commodity': 'Wheat'},
            {'season': 8, 'commodity': 'Barley'},
    ]
    return data 

def pandas_test():
    table_name = 'nass_commodity_area'
    
    columns, data = _get_data(table_name)

    df = pandas.DataFrame.from_records(data, columns=columns)

    # Fill nulls with zero:
    # df.fillna(0)
    # Or fill with "None":
    df = df.where((pandas.notnull(df)), None)

    return df.to_dict('records')
