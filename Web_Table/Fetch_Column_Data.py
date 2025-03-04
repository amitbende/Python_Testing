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

# Take a for loop for Row
for i in range(1, 5):
    a2 = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[" + str(i) + "]/td[1]")
    text = a2.text
    print(text)  # Kishore Manish Praveen Dheepthi

# Close the browser
driver.quit()
