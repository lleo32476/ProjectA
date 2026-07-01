from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Functions import button_class
from Functions import button_id
from Functions import input_class
from Functions import input_class_no_enter
import sys
import time
import re

lookup_item = "soap"

def search_savealot(street_num, street_name, city, state, zip_code, lookup_item):
    address = f"{street_num} {street_name.lower()}, {city.lower()}, {state.lower()} {zip_code}"
    print(address)
    options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get("https://savealot.com/")

    wait = WebDriverWait(driver, 10)

    time.sleep(2)
    
    # clicks store finder
    button_class("wp-block-navigation-item__label", wait, driver)

    # enters in zipcode and chooses nearest store
    input_class_no_enter("autocomplete__input autocomplete__input--default", zip_code, wait, driver)
    button_class("autocompleteInputId__option--0", wait, driver)

    

    input("Press Enter to close...")
    driver.quit()

search_savealot("1423", "Dual Highway", "Hagerstown", "MD", "21740", lookup_item)