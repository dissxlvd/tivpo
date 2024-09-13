import tkinter as tk
from tkinter import ttk

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


def main():
    root = tk.Tk()
    root.resizable(tk.FALSE, tk.FALSE)
    root.geometry('1200x900')
    root.configure(bg='#d0d0d0')

    contentFrame = ttk.Frame(root, padding=5, relief='sunken')
    contentFrame.grid(column=0, row=0)
    contentFrame.columnconfigure(0, weight=1)
    contentFrame.columnconfigure(1, weight=1)
    contentFrame.rowconfigure(0, weight=1)

    coinHolder = ttk.Frame(contentFrame, padding=10, height=400, relief='ridge')
    coinHolder.grid(column=0, row=0)

    btnHolder = ttk.Frame(contentFrame, padding=10, height=400, relief='ridge')
    btnHolder.grid(column=1, row=0)

    getDataBtn = ttk.Button(btnHolder, text='Get CMC data')
    getDataBtn.grid(column=0, row=0)

    quitBtn = ttk.Button(btnHolder, text='Quit', command=root.destroy)
    quitBtn.grid(column=0, row=1)

    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        root.title(response.headers.get('Date'))
        cmcResp = json.loads(response.text)

        # Dict
        # respStatus = cmcResp['status']

        # List
        respData = cmcResp['data']

        headerRank = ttk.Label(coinHolder, text='Rank')
        headerRank.grid(column=0, row=0)
        headerName = ttk.Label(coinHolder, text='Coin Name')
        headerName.grid(column=1, row=0)

        for i in range(len(respData)):
            print(respData[i])
            coinName = respData[i]['name']
            coinSymbol = respData[i]['symbol']
            coinRank = respData[i]['cmc_rank']
            coinPriceCurrent = respData[i]['quote']['RUB']['price']
            percentChange1h = respData[i]['quote']['RUB']['percent_change_1h']
            percentChange24h = respData[i]['quote']['RUB']['percent_change_24h']
            percentChange7d = respData[i]['quote']['RUB']['percent_change_7d']
            percentChange30d = respData[i]['quote']['RUB']['percent_change_30d']
            percentChange60d = respData[i]['quote']['RUB']['percent_change_60d']
            percentChange90d = respData[i]['quote']['RUB']['percent_change_90d']
            # print(coinName, coinSymbol, coinRank, coinPriceCurrent, percentChange1h, percentChange24h, percentChange7d,
            #       percentChange30d, percentChange60d, percentChange90d)

            testLabel = ttk.Label(coinHolder, text=coinRank)
            testLabel.grid(column=0, row=i+1)
            testLabel2 = ttk.Label(coinHolder, text=coinName)
            testLabel2.grid(column=1, row=i+1)
            textBtn = ttk.Button(coinHolder, text=coinSymbol + ' details', width=12)
            textBtn.grid(column=2, row=i+1)

    except (requests.ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
        print(e)

    root.mainloop()


main()
