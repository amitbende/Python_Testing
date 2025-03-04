import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# ChromeDriver Execution
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)     # Allowing the browser window to stay open after script execution
driver = webdriver.Chrome(options=options)          # Initializing the Chrome WebDriver

# Maximize Browser Window
driver.maximize_window()

# Open Facebook
driver.get("https://www.facebook.com/")

# Clicking the "Create New Account" link
create_account_link = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Create new account"))
)
create_account_link.click()

# Selecting a value from the month dropdown using Value attribute
month_dropdown = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.ID, "month"))
)
month_selector = Select(month_dropdown)     # Creating a Select element for interacting with the dropdown
month_selector.select_by_value("3")         # Selecting the March Month

# Adding a sleep to pause the script (you need to specify the sleep duration in seconds, e.g., time.sleep(2))
time.sleep(2)                                # Wait for 2 seconds

# Quitting the browser
driver.quit()
