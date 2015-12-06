'use strict';

angular.module('recApp', [])

.controller('RecommendCtrl', ['$scope', '$http', function($scope, $http) {

		$http.get('http://localhost:5000/api/lists').
			success(function(data) {

				$scope.items = data.lists;
				$scope.$apply();

			})

	}]);


;