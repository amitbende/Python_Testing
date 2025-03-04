from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://demo.guru99.com/test/drag_drop.html")

time.sleep(2)

driver.maximize_window()

# Identify source and destination elements
source_element = driver.find_element(By.XPATH, "//a[text()=' 5000']")
destination_element = driver.find_element(By.XPATH, "(//li[@class='placeholder'])[4]")

actions = ActionChains(driver)

# Perform drag-and-drop action
actions.drag_and_drop(source_element, destination_element).perform()

time.sleep(5)  # Adjust the wait time as needed

driver.quit()