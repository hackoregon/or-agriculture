cropApp.controller('choroplethCtrl', function($scope) {
  $scope.currentMap = 'assets/images/placeholder-map.png';

  $scope.maps = [
    {mapURL: 'assets/images/placeholder-map.png'},
    {mapURL: 'assets/images/nonirrigatedlandcapability_range.svg'},
    {mapURL: 'assets/images/usda_statsgo_crops.svg'}
  ];

  $scope.selectMap = function(index) {
    $scope.currentMap = $scope.maps[index].mapURL;
  };
});
