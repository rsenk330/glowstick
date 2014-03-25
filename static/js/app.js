(function() {
  'use strict';

  /**
    * Define a `format()` function on String that works like python's string
    * formatting.
    *
    * Example:
    *
    *    "hello {0} {1}".format(user.firstName, user.lastName);
    **/
  if (!String.prototype.format) {
    String.prototype.format = function() {
      var args = arguments;
      return this.replace(/{(\d+)}/g, function(match, number) {
        return typeof args[number] != 'undefined' ? args[number] : match;
      });
    };
  }

  angular.module('HashBangURLs', []).config(['$locationProvider', function($location) {
    $location.hashPrefix('!');
  }]);

  angular.module('glowstick', [
    'ngRoute',
    'ngResource',
    'ngProgressLite',
    'HashBangURLs',
    'common.directives',
    'devices.controllers',
    'devices.models',
    'home.controllers',
    'home.directives'
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
