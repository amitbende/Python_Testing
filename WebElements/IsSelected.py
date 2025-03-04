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

# Click Create new Account Button
driver.find_element(By.LINK_TEXT, "Create new account").click()

# Implicitly wait for 2 seconds
time.sleep(2)

# Verify Radio button is selected or not
RadioButton = driver.find_element(By.XPATH, "(//input[@class='_8esa'])[2]")

S1 = RadioButton.is_selected()
print("Is_Selected:", S1)

driver.quit()



