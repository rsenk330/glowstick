(function() {
  'use strict';

  angular.module("devices.models", []).factory("Device", function($resource, urls) {
    var Device = $resource(urls.devices + ":id");
    return Device;
  });
})();
