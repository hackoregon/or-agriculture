import random

import cropcompass as db
from flask import abort
import pandas




def _get_data(table_name, url_args={}):
    table_metadata = db.metadata_lookup(table_name)
    if not table_metadata:
        abort(404)
    row_keys = db.table_fields + (table_metadata['field'],)
    table_data = db.fetch_data(table_name, table_metadata, url_args)
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


def county_rankings():

    def random_percent():
        return float('%.2f' % random.random())

    data = [ 
        { 'category': 'Variety of Crops',
          'percent': random_percent() }, 
        { 'category': 'Percent of Farmable Land',
          'percent': random_percent() },
        { 'category': 'Revenue',
          'rawValue': '$43m',
          'percent': random_percent() }, 
        { 'category': 'Rain',
          'rawValue': '32in',
          'percent': random_percent() }, 
        { 'category': 'Growing Degree Days',
          'rawValue': '1200',
          'percent': random_percent() }, 
    ]

    return data
    

def farm_size():
    """
    JSON for farm size pie chart. Should look like this:
    {'total_farms': 300', 'farms_for_commodity': 25}

    @TODO still in progress
    """

    table_name = 'nass_commodity_farms'
    
    args = {'year': 2012,
            'region': 'Yamhill',
            'commodity': 'Walnuts'}
    columns, data = _get_data(table_name, args)
    df = pandas.DataFrame.from_records(data, columns=columns)

    # Fill nulls with zero:
    # df.fillna(0)
    # Or fill with "None":
    df = df.where((pandas.notnull(df)), None)

    # /data/nass_commodity_farms?region=Yamhill&limit=5000&commodity=Total Farms&year=2012
    # /data/nass_commodity_farms?region=Yamhill&limit=5000&commodity=Hazelnuts&year=2012

    # We don't have access to the original URL query params here,
    # so we grab the first commodity & region here

    selected_year = df.year.unique()[0]
    selected_commodity = df.commodity.unique()[0]
    selected_region = df.region.unique()[0]

    df = df[df.year == selected_year]
    df = df[df.region == selected_region]
    total_farms = df.pivot_table(index=['year', 'region', 'commodity'], values='farms', aggfunc=sum)

    df = df[df.commodity == selected_commodity]
    farms_for_commodity = df.pivot_table(index='region', values='farms', aggfunc=sum)

    #import ipdb; ipdb.set_trace()
    #return df.to_dict('records')
    return df.to_dict('records') 



def _shannon_entropy(pdist):
    """ Return Shannon Entropy of the probability pdist """
    # TODO add reference about Shannon Entropy
    return -sum(pdist * pandas.np.log2(pdist))


def crop_diversity():
    table_name = 'nass_commodity_area'
    default_year = 2012
    default_region = 'Yamhill'
    
    columns, data = _get_data(table_name)

    diversity = {}
    df = pandas.DataFrame.from_records(data, columns=columns)

    regions = df.region.unique()
    crops_and_acres = df[['commodity', 'acres']][df.year == default_year][df.region == default_region]
    croparea = crops_and_acres.groupby('commodity').sum()

    # Seems like the only way to fillna() with a regular "None"
    # which we have to do before serializing to JSON
    croparea = croparea.where((pandas.notnull(df)), None)

    data = croparea.to_dict('records')

    return data
