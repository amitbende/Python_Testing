import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# ChromeDriver Execution
options = webdriver.ChromeOptions()

# If path is true
options.add_experimental_option("detach", True)

# Object of chrome driver
driver = webdriver.Chrome(options=options)

# Maximize Window Browser
driver.maximize_window()

# Open FaceBook
driver.get("https://www.facebook.com/")

# path for login address
Username = driver.find_element(By.XPATH, "//input[@name='email']")

# Enter Address
Username.send_keys("amitbende123@gmail.com")

# Implicitly wait for 2 seconds
time.sleep(2)

# Clear Address
Username.clear()

# Implicitly wait for 2 seconds
time.sleep(2)

# Enter Address
Username.send_keys("amit@gmail.com")

# Implicitly wait for 2 seconds
time.sleep(2)

driver.quit()



