cropApp
  .controller('testCtrl', function($scope, $http, $log) {
    $http({
      method: 'GET',
      url: 'http://api.cropcompass.org/data/oain_harvest_acres?region=Benton',
      headers: {
        'Content-Type': 'text/html; charset=utf-8'
      }
    })
    
    .then(function(response) {
      $scope.harvestedAcres = response;
      console.log("hello");
      console.log(response.data.data);

    }, function() {
      console.log("I failed");
    });
  });

  // http://stackoverflow.com/questions/20987604/angular-iterate-over-json
