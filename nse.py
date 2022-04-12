import sys
import os
print("Hello, world")
sys.stdout.flush()
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
browser.get("https://www.nseindia.com/")
print((browser.title))
sys.stdout.flush()
browser.quit()
    
