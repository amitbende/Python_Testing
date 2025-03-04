from selenium import webdriver
import os
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver with download settings
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Define the directory where you want to save downloaded files
download_directory = os.path.join(os.getcwd(), "Download_Files")
prefs = {"download.default_directory": download_directory}
options.add_experimental_option("prefs", prefs)

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get("https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/")

# Maximize the browser window
driver.maximize_window()

# Wait for elements to load
driver.implicitly_wait(10)

# Click on the Zip file link
driver.find_element(By.PARTIAL_LINK_TEXT,"chromedriver_win32.zip").click()

# You may want to add a wait here to ensure the download completes
# before quitting the browser
# e.g., time.sleep(10)

# Quit the browser
driver.quit()
