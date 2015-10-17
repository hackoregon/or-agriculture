var cropApp = angular.module('cropApp', ['ngAnimate', 'ui.bootstrap', 'ui.router']);

cropApp
.factory('mySharedService', function($rootScope){
  var sharedService = [
    {name: 'Baker'}, {name:'Benton'}, {name: 'Clackamas'}, {name: 'Clatsop'}, {name: 'Columbia'}, {name: 'Coos'},
    {name: 'Crook'}, {name: 'Curry'}, {name: 'Deschutes'}, {name: 'Douglas'}, {name: 'Gilliam'}, {name: 'Grant'},
    {name: 'Harney'}, {name: 'Hood River'}, {name: 'Jackson'}, {name: 'Jefferson'}, {name: 'Josephine'}, {name: 'Klamath'},
    {name: 'Lake'}, {name: 'Lane'}, {name: 'Lincoln'}, {name: 'Linn'}, {name: 'Malheur'}, {name: 'Marion'}, {name: 'Morrow'},
    {name: 'Multnomah'}, {name: 'Polk'}, {name: 'Sherman'}, {name: 'Tillamook'}, {name: 'Umatilla'}, {name: 'Union'},
    {name: 'Wallowa'}, {name: 'Wasco'}, {name: 'Washington'}, {name: 'Wheeler'}, {name: 'Yamhill'}
  ];
  sharedService.county = '';

  sharedService.findCounty = function(cty) {
    this.county = cty;
    this.countyName();
  };

  sharedService.countyName = function() {
    $rootScope.$cc('foundCounty');
  };

  return sharedService;

});

function ControllerCounty($scope, sharedService) {
  $scope.ok() = function(cty) {
    sharedService.findCounty(cty);
  }

  $scope.$on('foundCounty', function() {
    $scope.county = sharedService.county;
  });
}

cropApp.controller('modalSelectCtrl', function($scope, sharedService, $uibModal, $log) {

  $scope.counties = [
    {name: 'Baker'}, {name:'Benton'}, {name: 'Clackamas'}, {name: 'Clatsop'}, {name: 'Columbia'}, {name: 'Coos'},
    {name: 'Crook'}, {name: 'Curry'}, {name: 'Deschutes'}, {name: 'Douglas'}, {name: 'Gilliam'}, {name: 'Grant'},
    {name: 'Harney'}, {name: 'Hood River'}, {name: 'Jackson'}, {name: 'Jefferson'}, {name: 'Josephine'}, {name: 'Klamath'},
    {name: 'Lake'}, {name: 'Lane'}, {name: 'Lincoln'}, {name: 'Linn'}, {name: 'Malheur'}, {name: 'Marion'}, {name: 'Morrow'},
    {name: 'Multnomah'}, {name: 'Polk'}, {name: 'Sherman'}, {name: 'Tillamook'}, {name: 'Umatilla'}, {name: 'Union'},
    {name: 'Wallowa'}, {name: 'Wasco'}, {name: 'Washington'}, {name: 'Wheeler'}, {name: 'Yamhill'}
  ];

  $scope.animationsEnabled = true;

  $scope.open = function(size) {
    var modalInstance = $uibModal.open({
      animation: $scope.animationsEnabled,
      templateUrl: 'angular/layout/modalSelect.html',
      controller: 'modalInstanceCtrl',
      size: size,
      resolve: {
        counties: function() {
          return $scope.counties;
        }
      }
    });
    modalInstance.result.then(function(selectedCounty) {
      $scope.selected = selectedCounty;
    }, function() {
      $log.info('Modal dismissed at: ' + new Date());
    });
  };
});

cropApp.controller('modalInstanceCtrl', function($scope, sharedService, $modalInstance, counties) {
  $scope.counties = counties;
  $scope.selected = {
    county: $scope.counties[0].name
  };

  $scope.ok = function() {
    $modalInstance.close($scope.selected.county);
  };

  $scope.cancel = function() {
    $modalInstance.dismiss('cancel');
  };
});

ControllerCounty.$inject = ['$scope', 'mySharedService'];