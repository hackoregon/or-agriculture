angular.module('cropApp')
.controller('countyRankingsCtrl', function($scope, $log, farmData) {

    $scope.rankings = [];

    var colorMap = {
        'Crop Diversity': '#F18A4B',
        'Variety of Crops': '#F18A4B',
        'Growing Degree Days': '#FBA46B',
        'Sunshine': '#FBA46B',
        'Revenue': '#3A8536',
        'Subsidies': '#3A8536'
    }

    $scope.$on('selectionChanged', function(event, selection) {

        farmData.getRelativeRankings(selection.county.name).then(function(result) {

            angular.forEach(result.data.data, function(item) {
                if (colorMap[item.category]) {
                    item.color = colorMap[item.category];
                }
            });

            $scope.rankings = result.data.data;
        });
    });

});
