import sys
import requests
print("Hello, world")
sys.stdout.flush()
url = "https://stackoverflow.com/questions/15767685/understanding-heroku-server-status-143"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response)
sys.stdout.flush()

    
