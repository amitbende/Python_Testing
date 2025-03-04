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
driver.get("file:///C:/Users/HP/Desktop/SDET/Test-form.html.html")

# Selecting a value from the city
City_dropdown = driver.find_element(By.XPATH, "//select[@id='multi_city']")

City = Select(City_dropdown)              # Creating a Select element for interacting with the dropdown
City.select_by_value("2")
City.select_by_value("4")
City.select_by_value("6")
City.select_by_value("8")

time.sleep(3)

# Deselect particular City
City.deselect_by_value("4")
City.deselect_by_value("6")
City.deselect_by_value("8")

# Adding a sleep to pause the script (you need to specify the sleep duration in seconds, e.g., time.sleep(2))
time.sleep(2)                                       # Wait for 2 seconds

# Quitting the browser
driver.quit()