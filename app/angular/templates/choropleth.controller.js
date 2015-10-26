cropApp.controller('choroplethCtrl', function($scope) {
  $scope.mapInfo = [
    {
      mapName: "Land Capability",
      mapDescription: "Land Capability Classification is a measure of the suitability of soils for field crops. The classification system was developed by the US Department of Agriculture to inform farm planning and soil manament. Soil is divided into eight capability classes, ranging from Class 1 (soils have slight limitations that restrict agricultural use) to Class 8 (soils or area are unsuitable for agriculture). With proper management, soils in classes 1-4 can be utilized to grow crops with long-term productivity, while soils in classes 4-8 are not suitable for commercial crop production and are best used for pasture, forestland, or non-agricultural uses.  Soils are classified for both irrigated and non-irrigated agriculture; the 'Land Capability' map on crop compass shows the soil classification for Oregon land suitable for growing commercial crops with irrigation. See [UDEL] for more information about each class."
    },
    {
      mapName: "Where crops are growing",
      mapDescription: "The USDA uses satellite imagery to create a map of where certain crops are growing and provides this information through the 'Cropland Data Layer' (CDL) program. According to the USDA (http://www.nass.usda.gov/research/Cropland/sarsfaqs2.html), The CDL is a raster, geo-referenced satellite imagery and extensive agricultural ground truth. In practice, the land is divided into pixels with 30-meter sides, and each pixel is determined to be growing a specific crop, or not, based on analysis of satellite imagery and verified by collecting on-the-ground data."
    }
  ];

  $scope.$on('selectionChanged', function(event, selection) {
    $scope.selection = selection;
  });

  $scope.showMapInfo = function(index) {
    $scope.currentMapName = $scope.mapInfo[index].mapName;
    $scope.currentMapDescription = $scope.mapInfo[index].mapDescription;
  };
});
