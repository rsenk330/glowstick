(function() {
  'use strict';

  angular.module('common.controllers', []).controller('NavigationController', ["$scope", "$location", function(scope, loc) {
    scope.isActive = function(l) {
      return l === loc.path();
    };

    scope.isChildActive = function(l) {
      return loc.path().indexOf(l) === 0;
    };
  }]);
})();
