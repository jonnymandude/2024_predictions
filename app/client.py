import requests

POLITICS_URL= "https://www.predictit.org/api/marketdata/all/"

class PoliticsClient(object):
    
    # Pretty simple request to send through the requests package
    def _get_request(self, url):
        response = requests.get(url)
        return response.json()
    
    
    # A parser for the markets
    def _parse_markets(self, markets):
        data = []
        
        for market in markets: 
            market_id = market['id']
            market_name = market['name']
            market_image = market['image']
            timestamp = market['timeStamp']
            for datum in market['contracts']:
                data_id = datum['id']
                data_name = datum['name']
                data_image = datum['image']
                price = datum['lastTradePrice']
                bestBuy = datum['bestBuyYesCost']
                bestSell = datum['bestSellYesCost']
                
                data.append(
                    {
                        'id': data_id,
                        'name': data_name,
                        'image': data_image,
                        'market_image': market_image,
                        'price': price,
                        'buy': bestBuy,
                        'sell': bestSell,
                        'timestamp': timestamp,
                        'market_id': market_id,
                        'market_name': market_name,
                    }
                )
        return data 
