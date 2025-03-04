from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ChromeDriver Execution
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()

# To enter URL/Open an Application
driver.get("https://www.google.com/")

# Wait
time.sleep(2)

# Enter "sky-bags"
search_box = driver.find_element(By.XPATH, "//textarea[@class='gLFyf']")
search_box.send_keys("skybags")

# Wait
time.sleep(2)

# Highlight All options
all_options = driver.find_elements(By.XPATH, "(//div[@class='OBMEnb'])[1]//li")

# Wait
time.sleep(2)

for option in all_options:  # Skybags  //skybags trolley bags  //skybags backpack
    text = option.text      # Skybags  //skybags trolley bags  //skybags backpack
    print(text)

    # skybags backpack
    if text == "skybags backpack":
        option.click()
        break

time.sleep(3)
driver.quit()