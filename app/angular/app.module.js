var cropApp = angular.module('cropApp', ['ngAnimate', 'ui.bootstrap', 'ui.router', 'chart.js'])
.config(['ChartJsProvider', function (ChartJsProvider) {
    // Configure all charts
    ChartJsProvider.setOptions({
      //colours: ['#FF5252', '#FF8A80'],
      scaleBeginAtZero: true,
      scaleFontSize: 16
    });
    // Configure all line charts
    ChartJsProvider.setOptions('Line', {
    });
  }]);
