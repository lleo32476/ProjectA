from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def button_class(class_name, wait, driver):
    try: 
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))
        time.sleep(2)
        button = driver.find_element(By.CLASS_NAME, class_name)
        button.click()
    except Exception:
        print("class: " + class_name + " error.")

def button_id(id, wait):
    try: 
        button = wait.until(EC.presence_of_all_elements_located((By.ID, id)))
        button[0].click()
    except Exception:
        print("id: " + id + " error.")

def input_class(class_name, input, wait, driver):
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
    element.click()
    element.send_keys(input)
    element.send_keys(Keys.RETURN)