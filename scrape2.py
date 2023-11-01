import selenium
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# server = Server("/Users/User101/browsermob-proxy-2.1.4/bin/browsermob-proxy")
# server.start()
# proxy = server.create_proxy()

def wait_for_element(driver, by, value, time_to_wait=10):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))


def click_element(driver, by, value):
    element = wait_for_element(driver, by, value)
    element.click()


def click_element_js(driver, by, value):
    element = driver.find_element(by, value)
    driver.execute_script('arguments[0].click();', element)

def send_keys_to_element(driver, by, value, keys):
    element = wait_for_element(driver, by, value)
    element.send_keys(keys)


def select_from_dropdown_by_index(driver, element_id, index):
    dropdown = Select(wait_for_element(driver, By.ID, element_id))
    dropdown.select_by_index(index)

def setup_webdriver():
    # Configure WebDriver to use the proxy
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
    # Initialize the WebDriver session
    # Make sure to pass the options

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

def close_webdriver(driver):
    driver.quit()


def scrape(person, driver):
 