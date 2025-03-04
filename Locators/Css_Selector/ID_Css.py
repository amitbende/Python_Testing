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

# First_Name
Username = driver.find_element(By.ID, "email")
Username.send_keys('Amit')

# Password
Password = driver.find_element(By.ID, "pass")
Password.send_keys('123456')

# Implicitly wait for 2 seconds
time.sleep(5)

driver.quit()



