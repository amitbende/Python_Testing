from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://demo.automationtesting.in/Frames.html")

time.sleep(2)

# Identify element and store it into an object
element_to_move = driver.find_element(By.XPATH, "//a[text()='SwitchTo']")

actions = ActionChains(driver)

# Wait
time.sleep(2)

# Move cursor to the element
actions.move_to_element(element_to_move).perform()

time.sleep(2)

# Click on the Windows Option after moving cursor
driver.find_element(By.XPATH, "//a[text()='Windows']").click()

time.sleep(5)  # Adjust the wait time as needed

driver.quit()