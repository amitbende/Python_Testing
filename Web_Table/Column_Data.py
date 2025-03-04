from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Open the URL/Application
driver.get("https://omayo.blogspot.com/")

# Use WebDriverWait to wait for elements to be visible
wait = WebDriverWait(driver, 10)  # You can adjust the timeout as needed

# Wait for the table to be visible
table = wait.until(EC.visibility_of_element_located((By.ID, "table1")))

# Take a for loop for Row
for i in range(1, 5):
    cell_locator = (By.XPATH, "//table[@id='table1']/tbody/tr[" + str(i) + "]/td[1]")
    a2 = wait.until(EC.visibility_of_element_located(cell_locator))
    text = a2.text
    print(text)  # Kishore Manish Praveen Dheepthi

# Close the browser
driver.quit()