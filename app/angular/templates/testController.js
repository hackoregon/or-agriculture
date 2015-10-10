cropApp
  .controller('testCtrl', function($scope, $http, $log) {
    $http({
      method: 'GET',
      url: 'http://api.cropcompass.org/data/subsidy_dollars?region=Benton',
      headers: {
        'Content-Type': 'text/html; charset=utf-8'
      }
    })
    // var test = $http.get('http://api.cropcompass.org/data/oain_harvest_acres?region=Benton', {headers:{'Accept':'application/json'}});

    .then(function(response) {
      $scope.subsidyDollars = response;
      console.log("hello");
      console.log(response);
    }, function() {
      console.log("I failed");
    });
  });

  // http://stackoverflow.com/questions/20987604/angular-iterate-over-json
