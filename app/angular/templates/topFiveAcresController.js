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

cropApp
  .filter('orderByAcres', function() {
    return function(items, field, reverse) {
    var filtered = [];
    angular.forEach(items, function(item) {
      filtered.push(item);
    });
    filtered.sort(function (a, b) {
      return (a[field] > b[field] ? 1 : -1);
    });
    if(reverse) filtered.reverse();
    return filtered;
  };
});
