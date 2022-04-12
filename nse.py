import sys
import os
print("Hello, world")
sys.stdout.flush()
import requests
url = "https://www.nseindia.com/"
r = requests.get(url)
print(r.status_code)
sys.stdout.flush()

    
