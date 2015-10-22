cropApp
  .controller('acresCtrl', function($scope, $http, $log) {

    $scope.fetchData = function(params) {
      $http({
        method: 'GET',
        url: 'http://api.cropcompass.org/data/oain_harvest_acres?region=' + params.county.name,
      })

      .then(function(response) {
        $scope.harvestedAcres = response;
        console.log("hello");
        console.log($scope);
        console.log(response.data.data);
      }, function() {
        $log.error('Failed to fetch data from api for county: ' + params.county.name);
      });
    }

    $scope.$on('selectionChanged', function(event, selection) {
        $scope.selection = selection;
        $log.info("Got selection chanage in Acres Controller:", selection);
        var params = selection;
        $scope.fetchData(params);
    });

});
