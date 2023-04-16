# Set the URL for the Binance markets page
url = "https://www.binance.com/en/markets/overview"

# Send a GET request to the URL and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table that contains the cryptocurrency data
table = soup.find("table", {"class": "css-1rhbuit-table"})

# Extract the rows from the table and remove the header row
rows = table.find_all("tr")[1:]

# Create a list to store the cryptocurrency data
cryptos = []

# Loop through each row and extract the cryptocurrency data
for row in rows:
    cells = row.find_all("td")
    name = cells[0].text.strip()
    pair = cells[1].text.strip()
    volume = cells[2].text.strip()
    price = cells[3].text.strip()
    change = cells[4].text.strip()
    buy = cells[5].text.strip()
    sell = cells[6].text.strip()
    cryptos.append({
        "name": name,
        "pair": pair,
        "volume": volume,
        "price": price,
        "change": change,
        "buy": buy,
        "sell": sell
    })

# Print the cryptocurrency data
for crypto in cryptos:
    print(f"Name: {crypto['name']}")
    print(f"Pair: {crypto['pair']}")
    print(f"Volume: {crypto['volume']}")
    print(f"Price: {crypto['price']}")
    print(f"Change: {crypto['change']}")
    print(f"Buy: {crypto['buy']}")
    print(f"Sell: {crypto['sell']}")
    print("---------------------")
