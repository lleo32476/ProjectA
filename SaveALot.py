from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Functions import button_class
from Functions import button_id
from Functions import input_class
import sys
import time
import re

# under works to create a scraper for all websites.
options = Options()
#options.add_argument("--headless")
#options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get("https://savealot.com/")

wait = WebDriverWait(driver, 10)

time.sleep(5)

FIND_STORE_PHRASES = [
    "select a store",
    "change store",
    "store finder",
    "find a store",
    "store locator",
    "my store",
    "change store",
    "in-store"
]

address = "21740"

## Change store
elements = driver.find_elements(By.TAG_NAME, "a")
for e in elements:
    text = e.text.strip().lower()
    for phrase in FIND_STORE_PHRASES:
        if phrase in text:
            e.click()
            break
    else:
        continue
    break

## input address
input_class("autocomplete__input autocomplete__input--default", address, wait, driver)
time.sleep(5)
button_class("autocomplete__option", wait, driver)

elements = driver.find_elements(By.TAG_NAME, "span")
for e in elements:
    text = e.text.strip().lower()
    print(e.get_attribute("class"))
    if "set as my store" in text:
        e.click()
        break


input("Press Enter to close...")
driver.quit()