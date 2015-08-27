#! /bin/bash

# cleanup
rm -fr states *.zip oregon.*

# download US counties
wget ftp://ftp2.census.gov/geo/tiger/TIGER2015/COUNTY/tl_2015_us_county.zip

# open QGIS to make the state shapefiles
mkdir -p states
echo "Starting QGIS ..."
echo "1. Add the zipfile as a vector layer."
echo "2. Split the layer on the STATEFP field into 'states'."
qgis

# make GeoJSON
ogr2ogr -f GeoJSON oregon.geojson states/tl_2015_*41.shp

# make TopoJSON
topojson -o oregon.topojson states/tl_2015_*41.shp
