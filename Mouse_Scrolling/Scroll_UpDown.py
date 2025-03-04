import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to the URL
driver.get("https://demo.guru99.com/test/guru99home/")

# Wait for elements to load
driver.implicitly_wait(10)

# Scroll Down: Use a positive pixel value
driver.execute_script("window.scrollBy(0, 1000)")

# Sleep for a few seconds (you can adjust the sleep time as needed)
time.sleep(5)

# Scroll Up: Use a negative pixel value
driver.execute_script("window.scrollBy(0, -500)")

# Optionally, you can adjust the pixel values to control the scroll amount

# Close the browser
driver.quit()
