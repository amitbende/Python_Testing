from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://demo.guru99.com/test/guru99home/")

# Wait for elements to load
driver.implicitly_wait(10)

# Identify the element up to which we want to scroll (Facebook)
s1 = driver.find_element(By.XPATH, "//*[text()='Facebook']")

# Execute JavaScript to scroll to the identified element
driver.execute_script("arguments[0].scrollIntoView();", s1)

# Optionally, you can scroll further by specifying scrollHeight value
# Example: driver.execute_script("window.scrollBy(0, 200);") to scroll 200 pixels down

# Close the browser
driver.quit()
