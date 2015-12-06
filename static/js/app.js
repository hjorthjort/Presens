'use strict';

angular.module('recApp', [])

.controller('RecommendCtrl', ['$scope', '$http', function($scope, $http) {

		$http.get('http://localhost:5000/api/lists').
			success(function(data) {
				$scope.list = data.lists[0].title;
				$scope.items = data.lists[0].items;
				$scope.$apply();

			})

	}]);


;