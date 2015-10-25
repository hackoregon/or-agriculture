(function () {
  'use strict';
  angular.module('cropApp').directive('simpleRadial', function () {
    return {
      restrict: 'EA',
      templateUrl: 'angular/components/simpleRadial.html',
      replace: true,
      scope: {
        percent: '=', // should range from 0..1
        value: '=',
        size: '=radialSize',
        title: '@',
        color: '@',
        icon: '@'
      },
      controller: function ($scope, $attrs) {
        $scope.viewModel = {
          formattedPercent: ''
        };

        $scope.radius = ($scope.size ? $scope.size/2 : 50);
        $scope.colors = [ '#83795D', '#D9D9D9' ];
        if ($scope.color != '') {
          $scope.colors[0] = $scope.color;
        }

        $scope.iconPosition = function(size) {
          var size = $scope.size;
          return {
            width: size + 'px',
            height: size + 'px',
            'margin-bottom': (0-size) + 'px'
          }
        }
      },
      link: function(scope, element) {

        var radius = scope.radius;
        var svg = d3.select(element[0]).append("svg")
          .attr("width", scope.size)
          .attr("height", scope.size)
        .append("g")
          .attr("transform", "translate("+radius+","+radius+")");

        var pie = d3.layout.pie().sort(null);

        var thickness = radius / 4;
        var arc = d3.svg.arc()
            .innerRadius(radius - 5 - thickness)
            .outerRadius(radius - 5);

        // invoke guard, prevent two changes from triggering simultaneous rendering
        var isRendering = false;
        var render = function() {
          if (!scope.percent) return;
          if (isRendering) return;
          isRendering = true;

          // for the visualization, clip to 100%
          var showPercent = d3.min([scope.percent, 1]);

          svg.empty();

          if (scope.icon == '') {
            var innerText = (!scope.value ? Math.round(100 * scope.percent) + '%' : scope.value);
            svg.append("text")
                .text(innerText)
                .attr("text-anchor", "middle")
                .style('font-size', radius/2)
                .attr('y', '0.3em')
                // .attr("dominant-baseline", "middle") // 'correct' alternative to y:.3em hack, but not supported by IE?
          }

          svg.selectAll("path")
              .data( pie([showPercent, 1.0-showPercent]) )
            .enter()
            .append("path")
              .attr("fill", function(d, i) { return scope.colors[ (i % scope.colors.length) ]} )
              .transition().duration(1000).ease('cubic')
              .attrTween("d", function(b) {
                var i = d3.interpolate({startAngle: 0, endAngle: 2*Math.PI}, b);
                return function(t) { return arc(i(t)); };
              });

          isRendering = false;
        }

        scope.$watch('percent', function(){
          render();            
        });
        scope.$watch('value', function() {
          render();
        });
      }
    };
  });

}).call(this);
