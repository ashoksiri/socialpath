
var socialpath = angular.module('SocialPath',['ui.router',])
    .controller('Dashboard',['$scope','$rootScope',function ($scope,$rootScope) {
        $scope.title ="Ashok"

}]).config(['$interpolateProvider','$stateProvider','$urlRouterProvider','$locationProvider',
        function($interpolateProvider,$stateProvider,$urlRouterProvider,$locationProvider) {
            $interpolateProvider.startSymbol('[#');
            $interpolateProvider.endSymbol('#]');

             $stateProvider
            .state('home', {
                url:  '/',
                controller: 'HomeController',
                templateUrl: 'home.html',
                controllerAs: 'vm'
            })

            .state('login', {
                url:  '/login',
                controller: 'LoginController',
                templateUrl: '/static/accounts/templates/login.html',
                controllerAs: 'vm'
            })

            .state('register', {
                url:  '/register',
                controller: 'RegisterController',
                templateUrl: '/static/accounts/templates/register.html',
                controllerAs: 'vm'
            }).state('dashboard', {
                url:  '/dashboard',
                controller: 'DashboardController',
                templateUrl: '/static/accounts/templates/index2.html',
                controllerAs: 'vm'
            });

            $urlRouterProvider.otherwise('/login');
  }]).controller('LoginController',function ($scope,$rootScope,$http) {
        $scope.user = {username:"ashok",screen_name:"developer"};

    }).controller('RegisterController',function ($scope,$rootScope, $http) {

        $scope.title = 'RegisterController';

    }).controller('DashboardController',function ($scope,$rootScope, $http) {

        $scope.title = 'DashboardController';

    });