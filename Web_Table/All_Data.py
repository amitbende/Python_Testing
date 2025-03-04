from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Open the URL/Application
driver.get("https://omayo.blogspot.com/")

# Wait for 2 seconds
time.sleep(2)

# Outer loop for rows
for i in range(1, 5, 1):
    # Inner loop for columns
    for j in range(1, 4, 1):
        # Locate the cell using XPath
        cell = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[" + str(i) + "]/td[" + str(j) + "]")

        # Get the text from the cell
        cell_text = cell.text
        print(cell_text, end=" ")
    print()

# Close the browser
driver.quit()
