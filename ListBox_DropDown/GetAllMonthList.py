from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

# ChromeDriver Execution
options = Options()
options.add_argument("--remote-allow-Origins=*")
options.add_argument("ignore-certificate-errors")
driver = webdriver.Chrome(service=Service("D:\Amit  Software Testing\Selenium Drivers\chromedriver_win32\chromedriver.exe"), options=options)

# To enter URL/Open an Application
driver.get("https://www.facebook.com/")

time.sleep(2)

# Click Create new Account Button
create_account_link = driver.find_element(By.XPATH, "//a[text()='Create new account']")
create_account_link.click()

time.sleep(2)

# Identify Listbox and store it into an object
month_dropdown = driver.find_element(By.XPATH, "//select[@id='month']")

# Create an object of Select Class
month_selector = Select(month_dropdown)

# Get text of all options
options_list = month_selector.options
for option in options_list:
    print(option.text)

# Quitting the browser
driver.quit()