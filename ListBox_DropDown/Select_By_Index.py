import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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
driver.find_element(By.XPATH, "//a[text()='Create new account']").click()

# Selecting a value from the month dropdown using indexing
month_dropdown = driver.find_element(By.ID, "month")
month_selector = Select(month_dropdown)              # Creating a Select element for interacting with the dropdown
month_selector.select_by_index(2)                    # Selecting the third option (index starts from 0)

# Adding a sleep to pause the script (you need to specify the sleep duration in seconds, e.g., time.sleep(2))
time.sleep(2)                                       # Wait for 2 seconds

# Quitting the browser
driver.quit()