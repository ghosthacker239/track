import requests
from bs4 import BeautifulSoup
import time

url = 'https://coinmarketcap.com/'

response = requests.get(url)
time.sleep(5)  # add a 5-second delay
soup = BeautifulSoup(response.content, 'html.parser')

print(response.content)  # print the HTML content for debugging

most_sold = soup.find('a', {'href': '/most-active-trading-pairs/'}).find_previous_sibling('div').get_text().strip()
most_bought = soup.find('a', {'href': '/most-active-trading-pairs/'}).find_next_sibling('div').get_text().strip()

print(f"The most sold cryptocurrency is {most_sold}.")
print(f"The most bought cryptocurrency is {most_bought}.")
