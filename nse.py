import sys
import os
import time
from selenium import webdriver

print("Hello, world")
sys.stdout.flush()

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36'
chrome_options.add_argument('--user-agent={0}'.format(user_agent))
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
browser.get("https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F&O")
time.sleep(3)
browser.find_element(By.LINK_TEXT,"Download (.csv)").click()
browser.quit()
    
