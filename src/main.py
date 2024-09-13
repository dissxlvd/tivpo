import math
import tkinter as tk
from tkinter import ttk

import requests
import json

import datafetch


def getDetails(coin, i):
    print(i)
    coinDetails = tk.Tk()
    coinDetails.title('coin '+coin.coinSymbol)

    coinPrice = ttk.Label(coinDetails, text='Price: '+str(round(coin.coinPriceCurrent, 3))+' RUB')
    coinPrice.pack()
    coinPC1h = ttk.Label(coinDetails, text='Percent change (1h): ' + str(round(coin.percentChange1h, 3)) + '%')
    coinPC1h.pack()
    coinPC24h = ttk.Label(coinDetails, text='Percent change (24h): ' + str(math.floor(coin.percentChange24h)) + '%')
    coinPC24h.pack()
    coinPC7d = ttk.Label(coinDetails, text='Percent change (7d): ' + str(round(coin.percentChange7d, 3)) + '%')
    coinPC7d.pack()
    coinPC30d = ttk.Label(coinDetails, text='Percent change (30d): ' + str(round(coin.percentChange30d, 3)) + '%')
    coinPC30d.pack()


def main():
    root = tk.Tk()
    root.resizable(tk.FALSE, tk.FALSE)
    root.configure(bg='#d0d0d0')
    root.title(datafetch.getDate())

    contentFrame = ttk.Frame(root, padding=5, relief='sunken')
    contentFrame.grid(column=0, row=0)
    contentFrame.columnconfigure(0, weight=1)
    contentFrame.columnconfigure(1, weight=1)
    contentFrame.rowconfigure(0, weight=1)

    coinHolder = ttk.Frame(contentFrame, padding=10, height=400, relief='ridge')
    coinHolder.grid(column=0, row=0)

    btnHolder = ttk.Frame(contentFrame, padding=10, height=400, relief='ridge')
    btnHolder.grid(column=1, row=0)

    coinBundle = datafetch.initData()
    getDataBtn = ttk.Button(btnHolder, text='Get CMC data', command=datafetch.initData)
    getDataBtn.grid(column=0, row=0)

    quitBtn = ttk.Button(btnHolder, text='Quit', command=root.destroy)
    quitBtn.grid(column=0, row=1)

    headerRank = ttk.Label(coinHolder, text='Rank')
    headerRank.grid(column=0, row=0)
    headerName = ttk.Label(coinHolder, text='Coin Name')
    headerName.grid(column=1, row=0)

    for i in range(len(coinBundle)):
        testLabel = ttk.Label(coinHolder,
                              text=coinBundle[i].coinRank)
        testLabel.grid(column=0, row=i+1)
        testLabel2 = ttk.Label(coinHolder,
                               text=coinBundle[i].coinName)
        testLabel2.grid(column=1, row=i+1)
        textBtn = ttk.Button(coinHolder,
                             text=coinBundle[i].coinSymbol + ' details',
                             width=12,
                             command=lambda: getDetails(coinBundle[i], i))
        textBtn.grid(column=2, row=i+1)

    root.mainloop()


main()
