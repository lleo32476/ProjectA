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
waiter = wait

time.sleep(2)

elements = driver.find_elements(By.XPATH, "//*[not(*)]")
for el in elements:
    try:
        text = el.text.strip().lower()
        class_name = el.get_attribute("class")
        if "change store" in text or "store finder" in text or "store" in text:
            print(f"Text: {el.text.strip()} | Class: {class_name}")
            button_class(class_name, waiter, driver)
    except:
        pass



#if "store" in body_text.lower():
    #shop_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Shop")
    #shop_button.click()

input("Press Enter to close...")
driver.quit()