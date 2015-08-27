# TopoJSON for all US counties:

To reproduce:

1. Download and unzip ftp://ftp2.census.gov/geo/tiger/TIGER2015/COUNTY/tl_2015_us_county.zip
2. Install node.js and npm.
3. At the command line, type

    ```
    sudo npm install -g topojson
    topojson -o counties.topojson tl_2015_us_county.shp
    ```

