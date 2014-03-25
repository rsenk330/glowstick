(function() {
  'use strict';

  var homeDirectives = angular.module("home.directives", []);

  homeDirectives.directive('videoPlayer', function() {
    return {
      restrict: 'E',
      templateUrl: PARTIALS_ROOT + "/video.html",
      controller: function($scope) {
        $scope.poster = "{0}/img/poster.jpg".format(STATIC_ROOT);

        var plugins = {
          chromecast: {},
        };
        var player = videojs('video', {'plugins': plugins, 'techOrder' : ['Html5', 'ChromecastTech']});

        $scope.$on('$destroy', function () {
          player.dispose();
        });
      }
    };
  });
})();
