(function() {
  'use strict';

  var deviceControllers = angular.module('devices.controllers', []);

  deviceControllers.controller('DeviceGetController', ["$scope", "$routeParams", "Device", "ngProgressLite", function(scope, routeParams, Device, progress) {
    progress.start();

    scope.device = Device.get({id: routeParams.id});
    scope.device.$promise.then(function() {
      scope.device_loaded = true;
      progress.done();
    });
  }]);

  deviceControllers.controller('DeviceListController', ["$scope", "Device", "ngProgressLite", function(scope, Device, progress) {
    progress.start();
    scope.devices = Device.query();
    scope.devices.$promise.then(function() {
      scope.devices_loaded = true;
      progress.done();
    }, function(data) {
      scope.devices_loaded = true;
      progress.done();
    });
  }]);
})();
