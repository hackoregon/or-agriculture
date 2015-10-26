import random

import cropcompass as db
from flask import abort
import pandas

DEFAULT_YEAR = 2012


def _get_data(table_name, url_args={}, as_dataframe=True):
    table_metadata = db.metadata_lookup(table_name)
    if not table_metadata:
        abort(404)
    row_keys = db.table_fields + (table_metadata['field'],)
    table_data = db.fetch_data(table_name, table_metadata, url_args)

    if as_dataframe:
        columns, data = row_keys, table_data

        df = pandas.DataFrame.from_records(data, columns=columns)

        # Fill NA values with a regular "None":
        # which we have to do before serializing to JSON
        df = df.where((pandas.notnull(df)), None)

        return df

    else:
        return row_keys, table_data


def test(url_args, **kwargs):
    data = [
            {'season': 5, 'commodity': 'Wheat'},
            {'season': 8, 'commodity': 'Barley'},
    ]
    return data 


def pandas_test(url_args, **kwargs):
    table_name = 'nass_commodity_area'
    
    df = _get_data(table_name)

    return df.to_dict('records')


def list_of_regions(url_args, **kwargs):
    regions = ['Baker', 'Benton', 'Clackamas', 'Clatsop', 'Columbia', 'Coos', 'Crook', 'Curry', 'Deschutes', 'Douglas', 'Gilliam', 'Grant', 'Harney', 'Hood River', 'Jackson', 'Jefferson', 'Josephine', 'Klamath', 'Lake', 'Lane', 'Lincoln', 'Linn', 'Malheur', 'Marion', 'Morrow', 'Multnomah', 'Polk', 'Sherman', 'Tillamook', 'Umatilla', 'Union', 'Wallowa', 'Wasco', 'Washington', 'Wheeler', 'Yamhill'] 

    regions = ['Oregon'] + sorted(regions)

    regions_data = [
            {'name': region} for region in regions]

    return regions_data


def list_of_commodities(url_args, **kwargs):
    commodities= ['Wheat', 'Grasses, Grass Seed, and Sod', 'Corn', 'Barley', 'Potatoes', 'Mint', 'Sweet Corn', 'Cut Christmas Trees', 'Beans', 'Peas', 'Oats', 'Onions', 'Sugarbeets', 'Hazelnuts', 'Pears', 'Grapes', 'Cherries', 'Blueberries', 'Blackberries', 'Hops', 'Raspberries', 'Canola', 'Cranberries', 'Apples', 'Strawberries', 'Squash & Pumpkins', 'Broccoli', 'Cauliflower', 'Mustard', ]

    commodities.sort()

    commodities_data = [
            {'name': c,
             'NASS_name': c,
             'OAIN_name': c,
             'CDL_name': c} for c in commodities]

    commodities_data = [
            {'name': 'Any',
             'NASS_name': None,
             'OAIN_name': None,
             'CDL_name': None}] + commodities_data

    return commodities_data



def county_rankings(url_args, **kwargs):

    selected_year = url_args.get('year', DEFAULT_YEAR)
    selected_commodity = url_args.get('commodity')
    selected_region = url_args.get('region')

    def random_percent():
        return float('%.2f' % random.random())

    data = []

    val = _get_crop_diversity(selected_region)
    min_ = 0
    max_ = 12
    ranking = val / (max_ - min_)
    
    data.append({'category': 'Effective # of Crops',
                 'rawValue': float('%.3f' % val),
                 'min': min_, 'max': max_,
                 'percent': ranking})

    val = _get_precipitation(selected_region)
    min_ = 0
    max_ = 90 
    ranking = val / (max_ - min_)
    
    data.append({'category': 'Annual Precipitation',
                 'rawValue': val,
                 'min': min_, 'max': max_,
                 'percent': ranking})

    val = _get_growing_degree_days(selected_region)
    min_ = 0
    max_ = 3000
    ranking = val / (max_ - min_)
    
    data.append({'category': 'Growing Degree Days',
                 'rawValue': val,
                 'min': min_, 'max': max_,
                 'percent': ranking})

    return data
    

def _num_farms_for_commodity(commodity, region):
    """
    Number of farms for a particular commodity within 
    a county/region or statewide.
    """
    
    table_name = 'nass_commodity_farms'
    
    if region and commodity:
        df = _get_data(table_name, {
                'commodity': commodity,
                'region': region,
                'year': DEFAULT_YEAR})

        total = df.pivot_table(
                index='region',
                values='farms',
                aggfunc=sum)

        if len(total):
            return total.values[0]
        else:
            return 0 

    elif commodity and not region:
        # Total num farms for commodity for all regions
        df = _get_data(table_name, {
                'commodity': commodity,
                'results': 9999,
                'year': DEFAULT_YEAR})

        # Exclude any rows with Total in them 
        df = df[~df.commodity.str.contains('Total')]
        
        total = df.pivot_table(
                index='commodity',
                values='farms',
                aggfunc=sum)

        if len(total):
            return total.values[0]
        else:
            return 0 

    else:
        # Not either was specified
        return 0


def _num_farms_for_region(region):
    """
    Total number of farms with any commodity within
    a county/region or statewide.
    """

    table_name = 'nass_commodity_farms'
    
    if region:
        df = _get_data(table_name, {
                'region': region,
                'year': DEFAULT_YEAR,
                'results': 9999})

        total = df.pivot_table(
                index='region',
                values='farms',
                aggfunc=sum)

        if len(total):
            return total.values[0]
        else:
            return 0 

    else:
        # Total farms for all regions (statewide)
        df = _get_data(table_name, {
                'commodity': 'Total farms',
                'year': DEFAULT_YEAR,
                'results': 9999})

        total = df.pivot_table(
                index='commodity',
                values='farms',
                aggfunc=sum)

        if len(total):
            return total.values[0]
        else:
            return 0 


def number_of_farms(url_args, **kwargs):
    """
    JSON for farm size pie chart. Should look like this:
    {'total_farms': 300', 'farms_for_commodity': 25}

    Sample query URLs:
    /data/nass_commodity_farms?region=Yamhill&limit=5000&commodity=Total Farms&year=2012
    /data/nass_commodity_farms?region=Yamhill&limit=5000&commodity=Hazelnuts&year=2012

    """

    selected_year = url_args.get('year', DEFAULT_YEAR)
    selected_commodity = url_args.get('commodity')
    selected_region = url_args.get('region')

    if 'oregon' in selected_region.lower():
        selected_region = None

    if 'any' in selected_commodity.lower():
        selected_commodity = None

    farms_for_commodity = _num_farms_for_commodity(selected_commodity, selected_region)
    total_farms = _num_farms_for_region(selected_region)

    data = {
        "region": selected_region or "Oregon",
        "commodity": "Farms with %s" % selected_commodity if selected_commodity else None,
        "year": selected_year,
        "farms_per_commodity": farms_for_commodity,
        "total_farms": total_farms,
    }

    return data


def _shannon_entropy(pdist):
    """ Return Shannon Entropy of the probability pdist """
    # TODO add reference about Shannon Entropy
    # return -sum(pdist * pandas.np.log2(pdist))
    return -sum(pdist * pandas.np.log(pdist))


def _effective_number_crops(pdist):
    """ 
    Returns effective number of crops given proportional distribution pdist.
    """
    return pandas.np.power(pandas.np.e, _shannon_entropy(pdist))


def _get_crop_diversity(region):
    """
    In progress
    """

    table_name = 'nass_commodity_area'
    
    diversity = {}
    df = _get_data(table_name, {
            'region': region,
            'year': DEFAULT_YEAR,
            'results': 9999})

    if len(df):
        number_of_crops = df.commodity.nunique()
        crops_and_acres = df[['commodity', 'acres']].dropna()
        croparea = crops_and_acres.groupby('commodity').sum()
        pdist = croparea.acres.astype(float) / sum(croparea.acres.astype(float))
        effective_crops = _effective_number_crops(pdist)
    else:
        return 0

    if pandas.np.isnan(effective_crops):
        import ipdb; ipdb.set_trace()
        return None
    else:
        return effective_crops#.to_dict('records')


def _get_production_over_time(region, commodity):
    data = {'commodity': commodity,
            'region': region,
            'years': []}

    if region:
        # All commodities for one region

        if commodity:
            # filter to one commodity
            values = [] 

        else:
            # sum all commodities for region
            values = []

    elif commodity:

        if region:
            values = []
        else:
            values = []

    else:
        # All commodities for all regions (statewide)
        # exclude totals?
        values = []

    data['years'] = values
    return data


def _get_growing_degree_days(region):
    return 0


def _get_precipitation(region):
    return 0


def production_over_time(url_args, **kwargs):

    selected_year = None 
    selected_commodity = url_args.get('commodity')
    selected_region = url_args.get('region')

    data = _get_production_over_time(selected_region, selected_commodity)

    return data
