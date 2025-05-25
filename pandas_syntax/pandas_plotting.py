# %%
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

plt.style.use("seaborn-v0_8")

# %%
df = yf.download(tickers="AAPL", interval="1d", multi_level_index=False)
df.index = pd.to_datetime(df.index.date)
print(df)

# %%
# Plotting the "Close" column of the dataframe
df.Close.plot()
plt.ylabel("Price in USD")
plt.xlabel("AAPL Price Chart")
plt.show()

# %%
# Plot "Close" and "Volume" columns of the dataframe
ax = df.loc[:, ["Close", "Volume"]].plot(secondary_y="Volume")
ax.set_ylabel("Volume")
ax.right_ax.set_ylabel("Price in USD")
ax.set_xlabel("year")
plt.show()
