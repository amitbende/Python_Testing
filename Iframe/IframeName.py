import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# ChromeDriver Execution
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()

# Open the URL
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

# Switch to the iframe
iframe = driver.find_element(By.NAME, "iframeResult")
driver.switch_to.frame(iframe)

# Wait
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Click me to display Date and Time']").click()

# Wait
time.sleep(2)

# Switch back to the main page
driver.switch_to.default_content()

# Click the Home Icon link
driver.find_element(By.ID, "tryhome").click()

# Wait
time.sleep(2)

# Close the browser
driver.quit()