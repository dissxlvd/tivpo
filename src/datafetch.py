import requests
import json


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '20',
    'convert': 'RUB'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '311b36ad-315d-4d41-80b1-cc6cc31646a8',
}


class Coin():
    coinName: str
    coinSymbol: str
    coinRank: str
    coinPriceCurrent: str
    percentChange1h: str
    percentChange24h: str
    percentChange7d: str
    percentChange30d: str
    percentChange60d: str
    percentChange90d: str


def initData():
    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        # root.title(response.headers.get('Date'))
        cmcResp = json.loads(response.text)
        respData = cmcResp['data']  # List
        coinBundle = []

        for i in range(len(respData)):
            coin = Coin()
            coin.coinName = respData[i]['name']
            coin.coinSymbol = respData[i]['symbol']
            coin.coinRank = respData[i]['cmc_rank']
            coin.coinPriceCurrent = respData[i]['quote']['RUB']['price']
            coin.percentChange1h = respData[i]['quote']['RUB']['percent_change_1h']
            coin.percentChange24h = respData[i]['quote']['RUB']['percent_change_24h']
            coin.percentChange7d = respData[i]['quote']['RUB']['percent_change_7d']
            coin.percentChange30d = respData[i]['quote']['RUB']['percent_change_30d']
            coin.percentChange60d = respData[i]['quote']['RUB']['percent_change_60d']
            coin.percentChange90d = respData[i]['quote']['RUB']['percent_change_90d']

            coinBundle.append(coin)

        for coin in range(len(coinBundle)):
            print(coinBundle[coin].coinName)

        return coinBundle

    except (requests.ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
        print(e)
