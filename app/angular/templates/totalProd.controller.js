cropApp
  .controller('totalProdCtrl', function($scope, $http, $log) {

    $scope.fetchData = function(params) {
        $http({

          method: 'GET',
          url: 'http://api.cropcompass.org/data/nass_commodity_area?year=2012&region=' + params.county.name,

        })
        .then(function(response) {

          $scope.updateChart(response.data.data);
          $log.debug(response.data.data);

        }, function() {

          $log.error('Failed to fetch data from api for county: ' + params.county.name);

        });
    };

    $scope.updateChart = function(data) {
        var labels = [],
            series = [],
            values = [];

        function onlyUnique(value, index, self) {
            return self.indexOf(value) === index;
        }

        for (var i=0; i < data.length; i++) {
            labels.push(data[i].commodity);
            series.push(data[i].year);
            values.push(data[i].acres);
        }

        $scope.labels = labels.filter( onlyUnique );
        $scope.series = series.filter ( onlyUnique );
        $scope.data = [values.filter( onlyUnique )];

        $log.debug( $scope.labels, $scope.series, $scope.data );
    };

    $scope.$on('selectionChanged', function(event, selection) {
        $scope.selection = selection;
        $log.info("Got selection chanage in Total Production Controller:", selection);
        var params = selection;
        $scope.fetchData(params);
    });

});
