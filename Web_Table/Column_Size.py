from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Open the URL/Application
driver.get("https://omayo.blogspot.com/")

# Wait for 2 seconds
time.sleep(2)

# Find column size
all_column_addresses = driver.find_elements(By.XPATH, "//table[@id='table1']//tr[1]/th")
column_count = len(all_column_addresses)
print(column_count)

# Close the browser
driver.quit()
