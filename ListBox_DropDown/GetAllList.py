from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

# ChromeDriver Execution
options = Options()
options.add_argument("--remote-allow-Origins=*")
options.add_argument("ignore-certificate-errors")
driver = webdriver.Chrome(service=Service("D:\Amit  Software Testing\Selenium Drivers\chromedriver_win32\chromedriver.exe"), options=options)

# To enter URL/Open an Application
driver.get("file:///C:/Users/HP/Desktop/SDET/Test-form.html.html")

# Maximize browser
driver.maximize_window()

# Wait
time.sleep(2)

# Identify Listbox and store it into an object
Cities = driver.find_element(By.XPATH, "//select[@id='multi_city']")

# Create an object of Select Class
City_selector = Select(Cities)

# Call the method
options_list = City_selector.options
for option in options_list:
    option_text = option.text
    print(option_text)

# Quitting the browser
driver.quit()