from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ChromeDriver Execution
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Maximize the browser window.
driver.maximize_window()

# Navigate to Google's homepage.
driver.get("https://www.google.com/")

# Wait for 2 seconds (you should use explicit waits instead).
time.sleep(2)

# Find the search input field by its name and send the search query.
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("apple")

# Wait for a moment (you should use explicit waits instead).
time.sleep(2)

# Find the suggestion list elements using an appropriate XPath.
suggestion_list = driver.find_elements(By.XPATH, "//div[@id='Alh6id']//li")

# Wait for a moment (you should use explicit waits instead).
time.sleep(2)

for suggestion in suggestion_list:
    suggestion_text = suggestion.text
    print(suggestion_text)

    if suggestion_text.lower() == "apple watch":
        suggestion.click()
        break

# Wait for a moment (you should use explicit waits instead).
# time.sleep(5)

# Close the browser window and quit the driver.
# driver.quit()

