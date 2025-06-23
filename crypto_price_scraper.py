import requests
import time
import pandas as pd

def get_crypto__price_data():

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin'
    res = requests.get(url)
    details = res.json()[0]
    data = {
            'price' : details['current_price'],
            'time' : time.strftime("%d-%b-%H:%M")    }
    return data
    
data = get_crypto__price_data()
df = pd.DataFrame([data])
df.to_csv('crypto_prices.csv', mode='a', header=False, index=False)