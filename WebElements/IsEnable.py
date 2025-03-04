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

# Implicitly wait for 2 seconds
time.sleep(2)

# Verify Logo Visible or not
Button = driver.find_element(By.XPATH, "//button[text()='Log in']")

S1 = Button.is_enabled()
print("is_enabled:", S1)

driver.quit()
