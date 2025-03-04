import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ChromeDriver Execution
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Maximize the browser window
driver.maximize_window()

# Open the URL
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

# Switch to the iframe using the iframe index
driver.switch_to.frame(0)

# Wait
time.sleep(2)

# Click the "Click me to display Date and Time" button
driver.find_element(By.XPATH, "//button[text()='Click me to display Date and Time']").click()

# Wait
time.sleep(2)

# Switch back to the parent frame (main page)
driver.switch_to.parent_frame()

# Click the Home Icon link
driver.find_element(By.ID, "tryhome").click()

# Wait
time.sleep(2)

# Close the browser
driver.quit()
