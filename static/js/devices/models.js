(function() {
  'use strict';

  angular.module("devices.models", []).factory("Device", function($resource, urls) {
    return $resource(urls.devices + ":id", {id: "@id"});
  });
})();
