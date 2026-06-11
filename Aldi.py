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

def search_aldi(address, lookup_item):
    options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.aldi.us/")

    wait = WebDriverWait(driver, 10)
    waiter = wait

    #dismiss cookie banner
    button_id("onetrust-accept-btn-handler", wait)

    #open in store locations
    in_store_btn = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@aria-haspopup='dialog']")))
    in_store_btn[5].click()

    #clicks zip code button to change address
    button_class("e-1wlht9u", wait, driver )

    #inputs address into location search bar
    input_class("e-t267xt", address, wait, driver)

    #check if the found address = your address
    new_address = address.replace(" ", "") #removes spaces and commas from address for easy comparison
    new_address = new_address.replace(",", "")
    print(address)
    print(new_address)

    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "e-616lx5"))) #locates all address to compare
    buttons = driver.find_elements(By.CLASS_NAME, "e-616lx5")
    aldi_address = buttons[0].get_attribute("textContent")
    aldi_address = aldi_address.replace(" " , "")
    aldi_address = aldi_address.replace("," , "")
    print(aldi_address)
    if aldi_address == new_address:
        buttons[0].click()
    else:
        print("Invalid Address")
        sys.exit()

    #submits/saves address
    button_class("e-1fg4opk", wait, driver)

    #chooses the nearest aldi
    time.sleep(2)
    button_class("e-5irn7x", wait, driver)
    buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
    shop_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Shop this store']]")))
    shop_btn.click()

    #search up item
    input_class("e-751jof", lookup_item, wait, driver)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-item-card-button='true']")))

    items = driver.find_elements(By.CSS_SELECTOR, "[data-item-card-button='true']")
    for i, item in enumerate(items):
        sentence = item.get_attribute('textContent')
        if lookup_item.lower() in sentence.lower():
            print(f"Item {i}: '{item.text}' | href: '{item.get_attribute('href')}'")

    #buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
    #for i, b in enumerate(buttons):
    #   print(f"Button {i}: {b.text}")
    #  print(f"  HTML: {b.get_attribute('html')}")

    input("Press Enter to close...")
    driver.quit()