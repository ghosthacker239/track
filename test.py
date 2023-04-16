import requests
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

most_sold = soup.find('div', {'class': 'cmc-table__column-name sc-1kxikfi-0 eTVhdN'}).get_text().strip()
most_bought = soup.find_all('div', {'class': 'cmc-table__column-name sc-1kxikfi-0 eTVhdN'})[1].get_text().strip()

print(f"The most sold cryptocurrency is {most_sold}.")
print(f"The most bought cryptocurrency is {most_bought}.")
