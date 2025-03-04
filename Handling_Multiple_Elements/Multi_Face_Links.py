from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ChromeDriver Execution
options = Options()
options.add_argument("--remote-allow-Origins=*")
options.add_argument("ignore-certificate-errors")
driver = webdriver.Chrome(service=Service("D:\Amit  Software Testing\Selenium Drivers\chromedriver_win32\chromedriver.exe"), options=options)

# maximize browser
driver.maximize_window()

# To enter URL/Open an Application
driver.get("https://www.facebook.com/")

# Wait
time.sleep(2)

# To get Text of All the Links
all_links = driver.find_elements(By.XPATH, "//a")                   # List of web elements representing links

for link in all_links:
    link_text = link.text
    print(link_text)

# Quitting the browser
driver.quit()