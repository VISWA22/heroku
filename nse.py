import sys
import os
print("Hello, world")
sys.stdout.flush()
import requests
url = "https://www.nseindia.com/"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response = requests.get(stock_url, headers=headers)
print(response)
sys.stdout.flush()

    
