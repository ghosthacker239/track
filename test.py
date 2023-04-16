import requests
from bs4 import BeautifulSoup

# Set the URL for the CoinMarketCap homepage
url = "https://coinmarketcap.com/"

# Send a GET request to the URL and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table that contains the cryptocurrency data
table = soup.find("table", {"id": "trending"})

# Extract the rows from the table and remove the header row
rows = table.find_all("tr")[1:]

# Create a list to store the cryptocurrency data
cryptos = []

# Loop through each row and extract the cryptocurrency data
for row in rows:
    cells = row.find_all("td")
    name = cells[1].text.strip()
    symbol = cells[2].text.strip()
    price = cells[3].text.strip()
    volume = cells[4].text.strip()
    market_cap = cells[5].text.strip()
    change_24h = cells[6].text.strip()
    cryptos.append({
        "name": name,
        "symbol": symbol,
        "price": price,
        "volume": volume,
        "market_cap": market_cap,
        "change_24h": change_24h
    })

# Sort the cryptocurrencies by highest buy and sell volumes
cryptos.sort(key=lambda x: float(x["volume"].replace(",", "")), reverse=True)
highest_buy = cryptos[0]
cryptos.sort(key=lambda x: float(x["volume"].replace(",", "")))
highest_sell = cryptos[0]

# Print the highest buying and selling cryptocurrencies
print("Highest buying cryptocurrency:")
print(f"Name: {highest_buy['name']}")
print(f"Symbol: {highest_buy['symbol']}")
print(f"Price: {highest_buy['price']}")
print(f"Volume: {highest_buy['volume']}")
print(f"Market Cap: {highest_buy['market_cap']}")
print(f"24h Change: {highest_buy['change_24h']}")
print("---------------------")
print("Highest selling cryptocurrency:")
print(f"Name: {highest_sell['name']}")
print(f"Symbol: {highest_sell['symbol']}")
print(f"Price: {highest_sell['price']}")
print(f"Volume: {highest_sell['volume']}")
print(f"Market Cap: {highest_sell['market_cap']}")
print(f"24h Change: {highest_sell['change_24h']}")   

