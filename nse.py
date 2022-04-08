print("Hello, world")
sys.stdout.flush()
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)
try:
    browser.get("www.nseindia.com/market-data/live-equity-market")
    print("Page title was '{}'".format(browser.title))
    sys.stdout.flush()
finally:
    browser.quit()
