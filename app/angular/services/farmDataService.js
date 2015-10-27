angular.module('cropApp').factory('farmData', function($http, $log) {

	var resultCache = {};
        var host = 'http://api.cropcompass.org';
        //var host = 'http://localhost:5000';

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

		getRegions: function() {
			return checkCache(host + '/charts/list_of_regions');
		},
		getCommodities: function() {
			return checkCache(host + '/charts/list_of_commodities');
		},
		getAcresHarvested: function(countyName, year) {
			var y = year || 2012;
                        var c = countyName || 'Oregon (Statewide)';
			var acresUrl = host + '/data/oain_harvest_acres?year=' + y + '&region=' + c;
			return checkCache(acresUrl);
		},
		getAnimalsPresent: function(countyName, year) {
			var y = year || 2012;
                        var c = countyName || 'Oregon (Statewide)';
			var animalsUrl = host + '/data/nass_animals_inventory?year=' + y + '&region=' + c;
			return checkCache(animalsUrl);
		},
		getRelativeRankings: function(countyName, year) {
			var y = year || 2012;
			var rankingUrl = host + '/charts/county_rankings?year=' + y + '&region='+countyName;
			return checkCache(rankingUrl);
		}
	}

});
