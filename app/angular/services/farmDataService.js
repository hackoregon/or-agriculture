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

		getAcresHarvested: function(countyName, year) {
			var y = year || 2012;
			var acresUrl = 'http://api.cropcompass.org/data/oain_harvest_acres?year=' + y + '&region=' + countyName;
			return checkCache(acresUrl);
		},
		getAnimalsPresent: function(countyName, year) {
			var y = year || 2012;
			var animalsUrl = 'http://api.cropcompass.org/data/nass_animals_inventory?year=' + y + '&region=' + countyName;
			return checkCache(animalsUrl);
		},
		getRelativeRankings: function(countyName, year) {
			var y = year || 2012;
			var rankingUrl = 'http://api.cropcompass.org/charts/county_rankings?year=' + y + '&region='+countyName;
			return checkCache(rankingUrl);
		}
	}

});
