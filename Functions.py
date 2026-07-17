from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time

def button_class(class_name, wait, driver):
    try: 
        css = "." + class_name.replace(" ", ".")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
        button = driver.find_element(By.CSS_SELECTOR, css)
        driver.execute_script("arguments[0].click();", button)
        button_success(class_name)
    except Exception:
        print("class: " + class_name + " error.")


def button_id(id, wait):
    try: 
        button = wait.until(EC.presence_of_all_elements_located((By.ID, id)))
        button[0].click()
        button_success(id)
    except Exception:
        print("id: " + id + " error.")

def input_class(class_name, input, wait, driver):
    css = "." + class_name.replace(" ", ".")
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css)))
    element.click()
    element.send_keys(input)
    element.send_keys(Keys.RETURN)
    button_success(class_name)

def input_class_no_enter(class_name, input, wait, driver):
    css = "." + class_name.replace(" ", ".")
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css)))
    element.click()
    element.send_keys(input)
    button_success(class_name)

def button_success(class_name):
    print(class_name + " success")

def get_address(street_address, city, state, zip_code):
    full_address = street_address + " " + city + " " + state + " " + zip_code
    return full_address

def search(driver, phrase_list):
    button_elements = driver.find_elements(By.TAG_NAME, "button")
    a_elements = driver.find_elements(By.TAG_NAME, "a")

    for e in button_elements + a_elements:
        text = e.text.strip().lower()
        for phrase in phrase_list:
            if phrase in text:
                e.click()
                break
        else:
            continue
        break

def print_web(driver, phrase_list):
    button_elements = driver.find_elements(By.TAG_NAME, "input")
    a_elements = driver.find_elements(By.TAG_NAME, "a")

    for e in button_elements + a_elements:
        text = e.text.strip().lower()
        for phrase in phrase_list:
            if phrase in text:
                print(e.text, e.get_attribute("class"))
                