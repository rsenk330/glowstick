(function() {
  'use strict';

  angular.module('glowstick', [
    'ngRoute',
    'ngResource',
    'home.controllers'
    ]).config(['$routeProvider', function($routeProvider) {
      $routeProvider.when('/', {templateUrl: PARTIALS_ROOT + '/home.html', controller: 'HomeController'});
      $routeProvider.when('/device/:id', {templateUrl: PARTIALS_ROOT + '/device.html', controller: 'DeviceController'});
      $routeProvider.otherwise({redirectTo: '/'});
    }]);
})();
