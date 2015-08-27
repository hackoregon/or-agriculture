# TopoJSON for all US counties:

To reproduce:

1. Download and unzip ftp://ftp2.census.gov/geo/tiger/TIGER2015/COUNTY/tl_2015_us_county.zip
2. Install node.js and npm.
3. At the command line, type
```
sudo npm install -g topojson
topojson -o counties.topojson tl_2015_us_county.shp
```
4. For Oregon data, install QGIS and use the "Split Vector Layer" operation on the state FIPS code. This gives you a shapefile for each state; Oregon is FIPS code 41. Then use 'ogr2ogr' to make GeoJSON and 'topojson' to make TopoJSON.  
