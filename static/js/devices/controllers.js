(function() {
  'use strict';

  var deviceControllers = angular.module('devices.controllers', []);

  deviceControllers.controller('DeviceGetController', ["$scope", "$routeParams", "Device", "ngProgressLite", function(scope, routeParams, Device, progress) {
    progress.start();

    scope.device = Device.get({id: routeParams.id});
    scope.device.$promise.then(function() {
      scope.device_loaded = true;
      progress.done();
    }, function() {
      scope.error = true;
      progress.done();
    });
  }]);

  deviceControllers.controller('DeviceListController', ["$scope", "Device", "ngProgressLite", function(scope, Device, progress) {
    progress.start();
    Device.query().$promise.then(function(devices) {
      scope.devices = devices;
      progress.done();
    }, function(data) {
      scope.devices = [];
      progress.done();
    });
  }]);
})();
