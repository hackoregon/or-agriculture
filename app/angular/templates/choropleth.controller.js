cropApp.controller('choroplethCtrl', function($scope) {
  $scope.currentMap = 'assets/images/placeholder-map.png';
  $scope.currentMapDescription = '';

  $scope.maps = [
    {
      mapURL: 'assets/images/placeholder-map.png',
      mapDescription: 'Veggies es placeholder lorem ipsum vos postulo essum magis kohlrabi.'
    },
    {
      mapURL: 'assets/images/nonirrigatedlandcapability_range.svg',
      mapDescription: 'Veggies es land capability lorem ipsum vos postulo essum magis kohlrabi.'
    },
    {
      mapURL: 'assets/images/usda_statsgo_crops.svg',
      mapDescription: 'Veggies es where crops can grow lorem ipsum vos postulo essum magis kohlrabi.'
    }
  ];

  $scope.selectMap = function(index) {
    $scope.currentMap = $scope.maps[index].mapURL;
    $scope.currentMapDescription = $scope.maps[index].mapDescription;
  };
});
