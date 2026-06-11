from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://savealot.com/")

input("Press Enter to close...")
driver.quit()