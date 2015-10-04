cropApp.config(function($stateProvider, $urlRouterProvider) {

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
});
