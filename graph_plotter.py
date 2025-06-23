from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/ZiaPrince2691/Crypto-price-tracker/refs/heads/main/crypto_prices.csv')
df = df.tail(7)
df.plot(x='time', y='price', marker='o')

plt.title("Crypto Price Tracker")
plt.xlabel("Time")
plt.ylabel("Price in USD")
plt.grid(True)
plt.show()