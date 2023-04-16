import requests
from bs4 import BeautifulSoup
import time

url = 'https://coinmarketcap.com/'

response = requests.get(url)
time.sleep(5)  # add a 5-second delay
soup = BeautifulSoup(response.content, 'html.parser')

most_sold = soup.find('div', {'class': 'cmc-table__column-name'}).get_text().strip()
most_bought = soup.find_all('div', {'class': 'cmc-table__column-name'})[1].get_text().strip()

print(f"The most sold cryptocurrency is {most_sold}.")
print(f"The most bought cryptocurrency is {most_bought}.")
