angular.module('cropApp').factory('farmData', function($http, $log) {

	var resultCache = {};

	function checkCache(url) {
		if (resultCache[url] != null) {
			return resultCache[url];
		}

		var result = $http.get(url);
		result.catch(function(err) {
			$log.error('Failed to fetch data at url: ' + url);
		})
		resultCache[url] = result;
		return result;
	}

	return {

		getAcresHarvested: function(countyName) {
			var acresUrl = 'http://api.cropcompass.org/data/oain_harvest_acres?region=' + countyName;
			return checkCache(acresUrl);
		},

		getRelativeRankings: function(countyName) {
			var rankingUrl = 'http://api.cropcompass.org/charts/county_rankings?region='+countyName;
			return checkCache(rankingUrl);
		}
	}

});
