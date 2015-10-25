import random

import cropcompass as db
from flask import abort
import pandas




def _get_data(table_name, url_args={}, as_dataframe=True):
    table_metadata = db.metadata_lookup(table_name)
    if not table_metadata:
        abort(404)
    row_keys = db.table_fields + (table_metadata['field'],)
    table_data = db.fetch_data(table_name, table_metadata, url_args)

    if as_dataframe:
        columns, data = row_keys, table_data

        if not len(data):
            abort(404)
        df = pandas.DataFrame.from_records(data, columns=columns)

        # Fill NA values with a regular "None":
        # which we have to do before serializing to JSON
        df = df.where((pandas.notnull(df)), None)

        return df

    else:
        return row_keys, table_data


def test():
    data = [
            {'season': 5, 'commodity': 'Wheat'},
            {'season': 8, 'commodity': 'Barley'},
    ]
    return data 


def pandas_test():
    table_name = 'nass_commodity_area'
    
    df = _get_data(table_name)

    return df.to_dict('records')


def list_of_regions():
    regions = ['Oregon (Statewide)', 'Baker', 'Benton', 'Clackamas', 'Clatsop', 'Columbia', 'Coos', 'Crook', 'Curry', 'Deschutes', 'Douglas', 'Gilliam', 'Grant', 'Harney', 'Hood River', 'Jackson', 'Jefferson', 'Josephine', 'Klamath', 'Lake', 'Lane', 'Lincoln', 'Linn', 'Malheur', 'Marion', 'Morrow', 'Multnomah', 'Polk', 'Sherman', 'Tillamook', 'Umatilla', 'Union', 'Wallowa', 'Wasco', 'Washington', 'Wheeler', 'Yamhill'] 

    # regions.sort()

    regions_data = [
            {'name': region} for region in regions]

    return regions_data


def list_of_commodities():
    commodities= ['Wheat', 'Grasses, Grass Seed, and Sod', 'Corn', 'Barley', 'Potatoes', 'Mint', 'Sweet Corn', 'Cut Christmas Trees', 'Beans', 'Peas', 'Oats', 'Onions', 'Sugarbeets', 'Hazelnuts', 'Pears', 'Grapes', 'Cherries', 'Blueberries', 'Blackberries', 'Hops', 'Raspberries', 'Canola', 'Cranberries', 'Apples', 'Strawberries', 'Squash & Pumpkins', 'Broccoli', 'Cauliflower', 'Mustard', ]

    commodities.sort()

    commodities_data = [
            {'name': c,
             'NASS_name': c,
             'OAIN_name': c} for c in commodities]

    return commodities_data



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
    

def number_of_farms():
    """
    JSON for farm size pie chart. Should look like this:
    {'total_farms': 300', 'farms_for_commodity': 25}

    @TODO still in progress
    """

    table_name = 'nass_commodity_farms'
    
    #args = {'year': 2007,
    #        'region': 'Yamhill',}

    df = _get_data(table_name)

    # /data/nass_commodity_farms?region=Yamhill&limit=5000&commodity=Total Farms&year=2012
    # /data/nass_commodity_farms?region=Yamhill&limit=5000&commodity=Hazelnuts&year=2012

    # We don't have access to the original URL query params here,
    # so we grab the first commodity & region here
    selected_year = df.year.unique()[0]
    selected_commodity = df.commodity.unique()[0]
    selected_region = df.region.unique()[0]

    # Make sure we filter down to selection
    df = df[df.year == selected_year]
    df = df[df.region == selected_region]
    df = df[df.commodity == selected_commodity]

    farms_per_commodity = df.pivot_table(
            index='region',
            values='farms',
            aggfunc=sum).values[0]


    # Do a 2nd query for Total Farms because if they
    # filtered by a specific commodity it gets excluded
    selected_commodity = 'Total Farms'
    args = {'region': selected_region,
            'commodity': selected_commodity}
    df = _get_data(table_name, args)

    # Make sure we filter down to selection
    df = df[df.year == selected_year]
    df = df[df.region == selected_region]
    df = df[df.commodity == selected_commodity]

    total_farms = df.pivot_table(
            index='region',
            values='farms',
            aggfunc=sum).values[0]


    json = [ {
        "region": selected_region,
        "commodity": selected_commodity,
        "year": selected_year,
        "farms_per_commodity": farms_per_commodity,
        "total_farms": total_farms,
    }]

    #import ipdb; ipdb.set_trace()
    #return df.to_dict('records')
    #return totals.to_dict('records') 
    return json



def _shannon_entropy(pdist):
    """ Return Shannon Entropy of the probability pdist """
    # TODO add reference about Shannon Entropy
    return -sum(pdist * pandas.np.log2(pdist))


def crop_diversity():
    table_name = 'nass_commodity_area'
    default_year = 2012
    default_region = 'Yamhill'
    
    df = _get_data(table_name)

    diversity = {}

    regions = df.region.unique()
    crops_and_acres = df[['commodity', 'acres']][df.year == default_year][df.region == default_region]
    croparea = crops_and_acres.groupby('commodity').sum()

    croparea = croparea.where((pandas.notnull(df)), None)

    data = croparea.to_dict('records')

    return data
