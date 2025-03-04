from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver with ChromeOptions
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Open URL
driver.get("https://skpatro.github.io/demo/links/")

# Maximize browser window
driver.maximize_window()

# Wait
time.sleep(2)

# Click New Tab Button - You missed the .click() method here
driver.find_element(By.NAME, "NewTab").click()

# Wait
time.sleep(2)

# Get window handles
handles_Ids = driver.window_handles
print("Handles_Ids:", handles_Ids)

# Switch to the new window
driver.switch_to.window(handles_Ids[1])
print("Child Window Id:", handles_Ids[1])

# Wait
time.sleep(2)

# Click Training Link
driver.find_element(By.XPATH, "(//span[text()='Training'])[1]").click()

# Wait
time.sleep(2)

# Switch back to the main window
driver.switch_to.window(handles_Ids[0])
print("Main Window Id:", handles_Ids[0])

# Wait
time.sleep(2)

# Click New Window Button - You missed the .click() method here
driver.find_element(By.XPATH, "//input[@name='NewWindow']").click()

# Wait
time.sleep(2)

# Quit the browser
driver.quit()