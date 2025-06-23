import requests
import time
import pandas as pd

def get_crypto__price_data():

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin'
    res = requests.get(url)
    details = res.json()[0]

    data = {
            'price' : details['current_price'],
            'date' : time.strftime("%M")
    }
    return data

crypto_data_list = []

while True:
    
    data = get_crypto__price_data()
    crypto_data_list.append(data)
    df = pd.DataFrame(crypto_data_list)
    df.to_csv('crypto_prices.csv')
    time.sleep(30)