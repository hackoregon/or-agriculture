cropApp.controller('choroplethCtrl', function($scope) {

  $scope.$on('selectionChanged', function(event, selection) {
    $scope.selection = selection;
  });
  // $scope.currentMap = 'assets/images/maps/oregon_county_outlines-simplified-aligned.svg';
  // $scope.currentMapDescription = '';
  //
  // $scope.maps = [
  //   {
  //     mapURL: 'assets/images/maps/oregon_county_outlines-simplified-aligned.svg',
  //     mapDescription: 'Veggies es county lines lorem ipsum vos postulo essum magis kohlrabi.'
  //   },
  //   {
  //     mapURL: 'assets/images/maps/irrigatedlandcapability_range-simplified-aligned.svg',
  //     mapDescription: 'Veggies es land capability lorem ipsum vos postulo essum magis kohlrabi.'
  //   },
  //   {
  //     mapURL: 'assets/images/maps/all_crops_from_CDL_2012-simplified-aligned.svg',
  //     mapDescription: 'Veggies es where crops can grow lorem ipsum vos postulo essum magis kohlrabi.'
  //   }
  // ];
  //
  // $scope.selectMap = function(index) {
  //   $scope.currentMap = $scope.maps[index].mapURL;
  //   $scope.currentMapDescription = $scope.maps[index].mapDescription;
  // };
});
