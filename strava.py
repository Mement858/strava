import os
import re
import sys
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



options = Options()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
driver = webdriver.Chrome(os.path.join(os.getcwd(), "chromedriver"))

def read_gpx():
    cwd = os.getcwd()
    with open(cwd, 'r') as f:
        yield f


def upload_gpx_to_strava(gpx_names):
    
    for i, gpx_name in enumerate(gpx_names):
        driver.get('https://labs.strava.com/gpx-to-route/#12/-122.44503/37.73651')

        driver.find_element_by_id("gpxFile").send_keys(os.path.join(os.getcwd(), gpx_name))

        time.sleep(15)

        if i == 0:
            driver.find_element_by_id("oauthButton").click()

            driver.switch_to.window(driver.window_handles[-1])

            ######### SET IT THESE PARAMETERS TO YOURS ########## 
            driver.find_element_by_id("email").send_keys("EMAIL")
            driver.find_element_by_id("password").send_keys("PASSWORD")

            login_button = driver.find_element_by_id("login-button")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            login_button.click()

            time.sleep(5)

            driver.switch_to.window(driver.window_handles[-1])

        driver.find_element_by_id("saveButton").click()
        time.sleep(5)

        driver.find_element_by_class_name("save-route").click()

        driver.find_element_by_id("name").send_keys("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b"+os.path.splitext(os.path.basename(gpx_name))[0])

        driver.find_element_by_class_name("reverse").click()

        time.sleep(5)
        
if __name__ == "__main__":
    gpx_files = list(read_gpx)
    upload_gpx_to_strava(gpx_files)
