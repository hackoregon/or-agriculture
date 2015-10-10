cropApp.config(function($stateProvider, $urlRouterProvider, $httpProvider) {

  $stateProvider
    .state('index', {
      url: "",
      views: {
        "navbar": {
          templateUrl: 'angular/layout/navbar.html',
        },
        "choropleth": {
          templateUrl: 'angular/templates/choropleth.html'
        },
        "topFive": {
          templateUrl: 'angular/templates/topFive.html'
        },
        "totalProd": {
          templateUrl: 'angular/templates/totalProd.html'
        },
        "footer": {
          templateUrl: 'angular/layout/footer.html'
        }
      }
    });
  $urlRouterProvider.otherwise("/");

  $httpProvider.defaults.useXDomain = true;
  delete $httpProvider.defaults.headers.common['X-Requested-With']; 

});
