from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('G:\Programming\Web Scraping\Projects\Crypto-price-tracker\crypto_prices.csv')

df.plot(x='date', y='price', marker='o')

plt.title("Crypto Price Tracker")
plt.xlabel("Time")
plt.ylabel("Price in USD")
plt.grid(True)
plt.show()