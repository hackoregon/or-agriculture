cropApp
  .controller('totalProdCtrl', function($scope, $http, $log) {

    $scope.fetchData = function(params) {
        var params = params || {county: {}, commodity: {}};
        var region  = params.county.name || '';
        var commodity = params.commodity.NASS_name || '';

        $http({

          method: 'GET',
          url: 'http://api.cropcompass.org/charts/acres_over_time?region='
            + region + '&commodity=' + commodity,

        })
        .then(function(response) {

          $scope.updateChart(response.data.data);
          //$log.debug('Raw data', response.data.data);

        }, function() {

          $log.error('Failed to fetch data from api for county: ' + params.county.name);

        });
    };

    $scope.updateChart = function(data) {

        data = data[0];

        $scope.labels = [];
        $scope.data = [[]];
        $scope.series = [data.label];

        
        for (var i=0; i < data.years.length; i++) {
            $scope.labels.push(data.years[i].year);
            $scope.data[0].push(data.years[i].harvested_acres);
        }

        $log.debug( $scope.labels, $scope.series, $scope.data );
    };

    $scope.$on('selectionChanged', function(event, selection) {
        $scope.selection = selection;
        $log.info("Got selection chanage in Total Production Controller:", selection);
        var params = selection;
        $scope.fetchData(params);
    });

    $scope.fetchData();
});
