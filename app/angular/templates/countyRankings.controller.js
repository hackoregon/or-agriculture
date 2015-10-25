angular.module('cropApp')
.controller('countyRankingsCtrl', function($scope, $log, farmData) {

    $scope.rankings = [];

    var colorMap = {
    	'Crop Diversity': '#F18A4B',
    	'Sunshine': '#FBA46B',
    	'Revenue': '#3A8536',
    	'Subsidies': '#3A8536'
    }

    $scope.$on('selectionChanged', function(event, selection) {
        //$log.info("Got selection chanage in Rankings Controller:", selection);
        farmData.getRelativeRankings(selection.county.name).then(function(result) {

        	//$log.info(result.data);

        	angular.forEach(result.data.data, function(item) {
        		if (colorMap[item.category]) {
        			item.color = colorMap[item.category];
        		}
        	});

          	$scope.rankings = result.data.data;
        });
    });

});
