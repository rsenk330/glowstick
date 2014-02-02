(function() {
  'use strict';

  angular.module('home.controllers', []).controller('HomeController', ["$scope", "$resource", "urls", function(scope, resource, urls) {
    var Device = resource(urls.devices);
    scope.devices = Device.query();
  }]).controller('DeviceController', ["$scope", "$resource", "$routeParams", "urls", function(scope, resource, routeParams, urls) {
    var Device = resource(urls.devices + ":id");
    scope.device = Device.get({id: routeParams.id});
  }]);
})();
