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

# Take a for loop for Column
for i in range(1, 4):
    a2 = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[" + str(i) + "]")
    text = a2.text
    print(text, end=" ")                    # Praveen // 29 // Bangalore
print()  # Print a new line after the loop

# Close the browser
driver.quit()
