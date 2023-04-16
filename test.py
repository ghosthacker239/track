import requests
import pandas as pd

# Set the API endpoint
url = "https://api.coinmarketcap.com/v1/ticker/"

# Make the API call to get the cryptocurrency data
response = requests.get(url)
data = response.json()

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Extract the columns we need
df = df[['name', 'symbol', 'price_usd', 'percent_change_24h']]

# Sort the data by the percent change in the last 24 hours
df = df.sort_values('percent_change_24h', ascending=False)

# Print the top 10 cryptocurrencies by percent change
print(df.head(10))
