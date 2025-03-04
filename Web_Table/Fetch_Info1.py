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

# Fetch "Pune"
s3 = driver.find_element(By.XPATH, "//table[@id='table1']//tbody/tr[2]/td[3]")
text = s3.text
print(text)

# Close the browser
driver.quit()
