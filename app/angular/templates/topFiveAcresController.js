angular.module('cropApp')
  .controller('acresCtrl', function($scope, $log, farmData) {

    $scope.dataSet = [];
    $scope.selected = '';
    $scope.category = 'acres';
    $scope.max_value = 1;

    $scope.convert = function(acres) {
      // multiply by 100 to create a percentage
      // but scale it back to allow for the number following the bar
      // (we don't want it to wrap to the next row)

      // Round that number to have it display more cleanly
      return Math.round(85*(acres/$scope.max_value)) + '%'
    }

    $scope.updateData = function(countyName, category) {

      var getData = (category == 'acres' ? farmData.getAcresHarvested(countyName)
                                         : farmData.getAnimalsPresent(countyName));

      getData.then(function(response) {
        $scope.dataSet = [];

        var max_value = 0;
        angular.forEach(response.data.data, function(val, key) {
          val.value = (category == 'acres' ? val.harvested_acres : val.animals);
          // there seems to be a lot of nulls in the data, don't include those
          if (!!val.value) {
            $scope.dataSet.push(val);
            max_value += val.value;
          }
        });
        $scope.dataSet.sort(function(a,b) {
          return b.value - a.value;
        });
        $scope.dataSet = $scope.dataSet.slice(0,5);
        $scope.max_value = max_value;
      });
    }

    $scope.viewByAcres = function() {
      $scope.category = 'acres';
    }
    $scope.viewByAnimals = function() {
      $scope.category = 'animals';
    }
    $scope.$on('selectionChanged', function(event, selection) {
        if (selection.county.name != $scope.selected) {
          //$log.info("Got selection chanage in Acres Controller:", selection);
          $scope.selected = selection.county.name;
        }
    });

    $scope.$watch('category', function(newVal) {
      $scope.updateData($scope.selected, newVal);
    })
    $scope.$watch('selected', function(newVal) {
      $scope.updateData(newVal, $scope.category);
    })

});
