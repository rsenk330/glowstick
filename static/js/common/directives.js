(function() {
  'use strict';

  var commonDirectives = angular.module('common.directives', []);

  commonDirectives.directive('navigation', function() {
    return {
      restrict: 'E',
      templateUrl: PARTIALS_ROOT + "/navigation.html",
      controller: function($scope, $location, Device) {
        Device.query().$promise.then(function(devices) {
          $scope.devices = devices;
        });

        $scope.isActive = function(l) {
          return l === $location.path();
        };

        $scope.isChildActive = function(l) {
          return $location.path().indexOf(l) === 0;
        };
      }
    };
  });
})();
