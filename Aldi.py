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

address = "1423 Dual Highway, Hagerstown MD 21740"
lookup_item = "soap"

def search_aldi(address, lookup_item):
    options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.aldi.us/")
    productsList = []

    wait = WebDriverWait(driver, 10)

    # dismiss cookie banner
    button_id("onetrust-accept-btn-handler", wait)

    # open in store locations
    in_store_btn = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@aria-haspopup='dialog']")))
    in_store_btn[5].click()

    # clicks zip code button to change address
    button_class("e-1wlht9u", wait, driver)

    # inputs address into location search bar
    input_class("e-t267xt", address, wait, driver)

    # check if the found address = your address
    new_address = address.replace(" ", "")
    new_address = new_address.replace(",", "")
                                      
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "e-616lx5")))
    buttons = driver.find_elements(By.CLASS_NAME, "e-616lx5")
    aldi_address = buttons[0].get_attribute("textContent")
    aldi_address = aldi_address.replace(" ", "")
    aldi_address = aldi_address.replace(",", "")
    if aldi_address == new_address:
        buttons[0].click()
    else:
        print("Invalid Address")
        sys.exit()

    # submits/saves address
    button_class("e-1fg4opk", wait, driver)

    # chooses the nearest aldi
    time.sleep(2)
    button_class("e-5irn7x", wait, driver)
    buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
    shop_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Shop this store']]")))
    shop_btn.click()
    time.sleep(3)

    button_class("e-182rjqr", wait, driver)

    # searches up item name
    input_class("e-751jof", lookup_item, wait, driver)
    
    time.sleep(3)
    productCards = driver.find_elements(By.CLASS_NAME, "e-egal4z")
    for card in productCards:
        line = card.text.split("\n")

        for i in range(len(line)):
            if "Current price" in line[i] and lookup_item.upper() in line[i+2].upper():
                price = line[i].replace("Current price: $", "")
                name = line[i+2]
                size = line[i+3]
                productsList.append({"name": name, "size": size, "price": price})   

    print(productsList)

    input("Press Enter to close...")
    driver.quit()

search_aldi(address, lookup_item)