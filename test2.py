import requests
import json

url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/ohlcv/historical?id=74&convertId=2781&timeStart=1649536800000&timeEnd=1649882400000'

response = requests.get(url)
chart_data = json.loads(response.content)

print(chart_data)