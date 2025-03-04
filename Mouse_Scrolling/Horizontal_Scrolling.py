from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://demo.guru99.com/test/guru99home/scrolling.html")

# Wait for elements to load
driver.implicitly_wait(10)

# Maximize the browser window
driver.maximize_window()

# Identify the element up to which we want to scroll (VBScript)
s1 = driver.find_element(By.XPATH, "//a[text()='VBScript']")

# Sleep for a few seconds (you can adjust the sleep time as needed)
time.sleep(5)

# Execute JavaScript to scroll to the identified element
driver.execute_script("arguments[0].scrollIntoView();", s1)

# Optionally, you can scroll further by specifying scrollLeft value
# Example: driver.execute_script("window.scrollBy(200, 0);") to scroll 200 pixels to the right
driver.execute_script("window.scrollBy(200, 0);")

# Close the browser
driver.quit()