from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('G:\Programming\Web Scraping\Crypto Price Tracker\Crypto-price-tracker\crypto_prices.csv')

df.plot(x='time', y='price', marker='o')

plt.title("Crypto Price Tracker")
plt.xlabel("Time")
plt.ylabel("Price in USD")
plt.grid(True)
plt.show()