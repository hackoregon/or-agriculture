cropApp
  .controller('farmSizeCtrl', function($scope, $http, $log) {

    $scope.fetchData = function(params) {
        var params = params || {county: {}, commodity: {}};
        var region  = params.county.name || '';
        var commodity = params.commodity.NASS_name || '';

        $http({
          method: 'GET',
          url: 'http://api.cropcompass.org/charts/number_of_farms?region=' 
            + region + '&commodity=' + commodity,
        })
        .then(function(response) {

          $scope.updateChart(response.data.data);
          $log.debug(response.data.data);

        }, function() {

          $log.error('Failed to fetch data from api for county: ' + params.county.name);

        });
    };

    $scope.updateChart = function(data) {

        data = data[0];

        $scope.labels = ['Total farms in ' + data.region, data.commodity]
        $scope.data = [data.total_farms, data.farms_per_commodity];

        $log.debug( "Num farms", $scope.labels, $scope.data );
    };

    $scope.$on('selectionChanged', function(event, selection) {
        $scope.selection = selection;
        var params = selection;
        $scope.fetchData(params);
    });

    $scope.fetchData();

});
