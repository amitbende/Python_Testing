from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# ChromeDriver Execution
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)     # Allowing the browser window to stay open after script execution
driver = webdriver.Chrome(options=options)          # Initializing the Chrome WebDriver

# To enter URL/Open an Application
driver.get("file:///C:/Users/HP/Desktop/SDET/Test-form.html.html")

# Maximize browser
driver.maximize_window()

# Wait
time.sleep(2)

# Identify Listbox and store it into an object
Cities = driver.find_element(By.XPATH, "//select[@id='multi_city']")

# Create an object of Select Class
MultiSelect_City = Select(Cities)

# Selecting options by index
MultiSelect_City.select_by_index(0)
MultiSelect_City.select_by_index(2)
MultiSelect_City.select_by_index(3)
MultiSelect_City.select_by_index(5)
MultiSelect_City.select_by_index(6)
MultiSelect_City.select_by_index(7)

# Get First Select Option
First = MultiSelect_City.first_selected_option
First_Option = First.text
print(First_Option)

# Wait
time.sleep(2)

# Quitting the browser
driver.quit()
