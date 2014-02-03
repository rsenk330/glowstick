(function() {
  'use strict';

  angular.module('HashBangURLs', []).config(['$locationProvider', function($location) {
    $location.hashPrefix('!');
  }]);

  angular.module('glowstick', [
    'ngRoute',
    'ngResource',
    'ngProgressLite',
    'HashBangURLs',
    'common.controllers',
    'devices.controllers',
    'devices.models',
    'home.controllers'
    ]).config(['$routeProvider', function($routeProvider) {
      $routeProvider.when('/', {templateUrl: PARTIALS_ROOT + '/home.html', controller: 'HomeController'});
      $routeProvider.when('/devices', {templateUrl: PARTIALS_ROOT + '/devices.html', controller: 'DeviceListController'});
      $routeProvider.when('/devices/:id', {templateUrl: PARTIALS_ROOT + '/device.html', controller: 'DeviceGetController'});
      $routeProvider.when('/guide', {templateUrl: PARTIALS_ROOT + '/guide.html', controller: 'GuideController'});
      $routeProvider.when('/recordings', {templateUrl: PARTIALS_ROOT + '/recordings.html', controller: 'RecordingsController'});
      $routeProvider.when('/settings', {templateUrl: PARTIALS_ROOT + '/settings.html', controller: 'SettingsController'});
      $routeProvider.otherwise({redirectTo: '/'});
    }]);
})();
