cropApp.controller('modalSelectCtrl', function($scope, $uibModal, $log, $rootScope, farmData) {

  $scope.commodities = [];
  $scope.counties = [];
  $scope.selected = {
    commodity: {},
    county: {}
  }

  farmData.getRegions().then(function(result) {
    $scope.counties = result.data.data;
  });
  farmData.getCommodities().then(function(result) {
    $scope.commodities = result.data.data;
    if ($scope.commodities.length > 0) {
      $scope.selected.commodity = $scope.commodities[0];
    }
  });

  $scope.animationsEnabled = true;

  $scope.open = function(size, groupSet) {
    var group = groupSet || 'region';
    var modalInstance = $uibModal.open({
      animation: $scope.animationsEnabled,
      templateUrl: 'angular/layout/modalSelect.html',
      controller: 'modalInstanceCtrl',
      size: size,
      resolve: {
        counties: function() {
          return (group == 'region' ? $scope.counties : $scope.commodities);
        },
        title: function() {
          return (group == 'region' ? "Pick a Region or County" : "Select a Specific Crop");
        },
        header: function() {
          return (group == 'region' ? "Oregon Counties" : "Oregon Crops");
        }
      }
    });
    modalInstance.result.then(function(selected) {
      if (groupSet == 'region') {
        $scope.selected.county = selected.county;
      } else {
        $scope.selected.commodity = selected.county;
      }

      $rootScope.$broadcast('selectionChanged', $scope.selected);
      $log.debug($scope.selected);
      
    }, function() {
      $log.info('Modal dismissed at: ' + new Date());
    });
  };

  $scope.friendlyCounty = function() {
    if ($scope.selected && !!$scope.selected.county && $scope.selected.county.name) {
      return $scope.selected.county.name + ' County';
    }
    return "Oregon";
  }

  $scope.$on('selectCounty', function() {
      $scope.open('lg');
  });
});

cropApp.controller('modalInstanceCtrl', function($scope, $modalInstance, counties, title, header) {

  $scope.title = title;
  $scope.header = header;
  $scope.dataSet = counties;
  $scope.selected = {
    item: $scope.dataSet[0]
  };

  $scope.select = function(item) {
    $scope.selected.county = item;
    $scope.ok();
  }

  $scope.ok = function() {
    $modalInstance.close($scope.selected);
  };

  $scope.cancel = function() {
    $modalInstance.dismiss('cancel');
  };
});
