import sys
import requests
print("Hello, world")
sys.stdout.flush()
url = "https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F&O"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36'}
response = requests.get(url, headers=headers)
print(response)
sys.stdout.flush()

    
