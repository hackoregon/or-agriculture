cropApp
  .controller('testCtrl', function($scope, $http, $log) {
    $http({
      method: 'GET',
      url: 'http://api.cropcompass.org/data/subsidy_dollars?region=Oregon%20(Statewide)'
    }).then(function successCallback(response) {
      $scope.subsidyDollars = response;
      console.log(response);
    });
  });

  // http://stackoverflow.com/questions/20987604/angular-iterate-over-json
