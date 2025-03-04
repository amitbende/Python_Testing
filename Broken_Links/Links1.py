# pip install selenium requests

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# To enter URL/Open an Application
driver.get("http://www.deadlinkcity.com/")

# Wait
driver.implicitly_wait(10)

# Identify all links
all_links = driver.find_elements(By.TAG_NAME, "a")

for link in all_links:
    url = link.get_attribute("href")

    print("----------------------------------------------------")
    print(url)

    if url is None or url == "":
        print("URL is empty")
        continue

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check the response status code
        if response.status_code >= 400:
            print(url + " is broken")
        else:
            print(url + " is valid")
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print("Exception: " + str(e))

driver.quit()