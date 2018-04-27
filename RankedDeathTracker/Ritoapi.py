import requests
import ritoapiconst as Consts

class Ritoapi(object):

    def __init__(self, api_key, region=Consts.REGIONS['EUW']):
        self.api_key = api_key
        self.region = region

    def _requests(self, api_url, args, params={}):
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                region=self.region,
                url=api_url
                ),
            params=args
            )   
        return response.json()
    
    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
	        summonerName=name
	    )
        args = {'api_key': self.api_key}
        return self._requests(api_url, args)

    def get_rank_by_summonerid(self, id):
        api_url = Consts.URL['positions_by_summoner'].format(
	        summonerId=id
	    )
        args = {'api_key': self.api_key}
        return self._requests(api_url, args)

    def get_current_game(self, id):
        api_url = Consts.URL['current_game_data'].format(
	        summonerId=id
	    )
        args = {'api_key': self.api_key}
        return self._requests(api_url, args)

    def get_past_20_ranked_solo(self, id):
        api_url = Consts.URL['match_by_queue'].format(
            accountId=id
            )
        args = {'queue': Consts.QUEUE['SOLO'], 
                'season': Consts.SEASON['Season'], 
                'api_key': self.api_key
               }
        return self._requests(api_url, args)

    def get_maps(self):
        api_url = Consts.URL['maps']
        args = {'api_key': self.api_key}
        return self._requests(api_url, args)