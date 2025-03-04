from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://www.flipkart.com/")

time.sleep(2)

driver.maximize_window()

# Close Hidden division pop-up
close_button = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
close_button.click()

time.sleep(2)

# Identify element and store it into an object
element_to_left_click = driver.find_element(By.XPATH, "//a[@class='_3SkBxJ']")

actions = ActionChains(driver)

# Wait
time.sleep(2)

# Perform left-click
actions.click(element_to_left_click).perform()

time.sleep(5)  # Adjust the wait time as needed

driver.quit()