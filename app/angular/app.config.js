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
        }
      }
    });
  $urlRouterProvider.otherwise("/");
});
