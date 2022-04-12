import sys
import os
print("Hello, world")
sys.stdout.flush()
from selenium import webdriver
#from selenium import WebDriverWait
#from selenium.webdriver import ActionChains
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
chrome_options.add_argument('user-agent={0}'.format(user_agent))
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
#wait = WebDriverWait(driver, 20)
#action = ActionChains(driver)
browser.get("https://linuxtut.com/en/69f8734d0667d4621406/")
print((browser.title))
sys.stdout.flush()
browser.quit()
    
