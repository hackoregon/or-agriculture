cropApp
  .controller('acresCtrl', function($scope, $http, $log) {
    $http({
      method: 'GET',
      url: 'http://api.cropcompass.org/data/oain_harvest_acres?region=',
      headers: {
        'Content-Type': 'text/html; charset=utf-8'
      }
    })

    .then(function(response) {
      $scope.harvestedAcres = response;
      console.log("hello");
      console.log($scope);
      console.log(response.data.data);
    }, function() {
      console.log("I failed");
    });
});
