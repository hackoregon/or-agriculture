### Crop Compass API v2

#### Example queries:

GET /crop_sales_by_year

GET /crop_sales/?commodity_desc=WHEAT&county_name=BENTON

GET /crop_production/?unit_desc=ACRES

GET /crop_production/?unit_desc=ACRES&year=2007

GET /nass_raw/?search=sales

GET /nass_raw/?search=Silage

GET /nass_raw/?search=Winter

GET /nass_raw/?year=2012&search=eggs


#### To add a new endpoint / JSON view:

Add a view method here: `cropcompass/views.py`

Add a URL entry here: `cropcompass/urls.py`

Check out the examples for serveral types of view strategies. There are no examples that make a raw SQL query, but that can happen as well.
