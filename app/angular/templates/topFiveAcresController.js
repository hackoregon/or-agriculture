cropApp
  .controller('acresCtrl', function($scope, $http, $log) {

    $scope.convert = function(acres) {
      console.log('graph');
      return 100*(acres/$scope.total_acres) + '%'
    }

    $scope.fetchData = function(params) {
      $http({
        method: 'GET',
        url: 'http://api.cropcompass.org/data/oain_harvest_acres?region=' + params.county.name,
      })

      .then(function(response) {
        $scope.harvestedAcres = response;
        var total_acres = 0;
        angular.forEach(response.data.data, function(val, key) {
          total_acres += val.harvested_acres
        });
        $scope.total_acres = total_acres;
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
