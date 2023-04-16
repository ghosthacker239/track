import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Send GET request to webpage and retrieve HTML content
url = 'https://coinmarketcap.com/currencies/dogecoin/?period=7d'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract chart data
chart_data = soup.find('script', id='__NEXT_DATA__').string
chart_data = chart_data.replace('window.__INITIAL_STATE__=', '').replace(';', '')
chart_data = json.loads(chart_data)
chart_data = chart_data['cryptocurrency']['ohlcvHistorical'][::-1]

# Convert chart data to Pandas dataframe
df = pd.DataFrame(chart_data, columns=['time', 'open', 'high', 'low', 'close', 'volume', 'market_cap'])
df['time'] = pd.to_datetime(df['time'], unit='ms')

# Calculate moving average
ma = df['close'].rolling(window=20).mean()

# Plot moving average and candlestick chart
fig, ax = plt.subplots()
ax.plot(df['time'], df['close'], label='Dogecoin')
ax.plot(df['time'], ma, label='Moving Average')
ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.set_title('Dogecoin Price Chart')

# Fit linear regression model to predict future trends
model = LinearRegression()
X = df['time'].values.reshape(-1, 1)
y = df['close'].values.reshape(-1, 1)
model.fit(X, y)
future_dates = pd.date_range(start='2023-04-17', end='2023-05-17')
future_dates = future_dates.to_series()
future_dates = future_dates.dt.strftime('%Y-%m-%d')
future_dates = pd.to_datetime(future_dates)
future_dates = future_dates.values.reshape(-1, 1)
predictions = model.predict(future_dates)

# Plot predicted trends
fig, ax = plt.subplots()
ax.plot(df['time'], df['close'], label='Dogecoin')
ax.plot(future_dates, predictions, label='Predictions')
ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.set_title('Dogecoin Price Predictions')

# Estimate best time to buy based on predictions and current price
current_price = df['close'].iloc[-1]
best_time_to_buy = future_dates[predictions.argmin()]
print("The current price of Dogecoin is ${:.2f}.".format(current_price))
print("The estimated best time to buy Dogecoin is on {}.".format(best_time_to_buy.strftime('%Y-%m-%d')))
