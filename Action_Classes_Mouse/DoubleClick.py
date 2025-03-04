from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://demo.guru99.com/test/simple_context_menu.html")

time.sleep(2)

# Identify element and store it into an object
element_to_double_click = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")

actions = ActionChains(driver)

# Wait
time.sleep(2)

# Perform double-click
actions.double_click(element_to_double_click).perform()

time.sleep(5)  # Adjust the wait time as needed

driver.quit()