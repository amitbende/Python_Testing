import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver for Chrome
options = webdriver.ChromeOptions()

# The "detach" option is not valid, so we can just remove it
driver = webdriver.Chrome(options=options)

# Maximize the browser window
driver.maximize_window()

# Open the URL
driver.get("https://www.flipkart.com/search?q=oneplus+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=...")

# Wait for some time to allow the page to load
time.sleep(2)

# Get the review
review_element = driver.find_element(By.XPATH, "((//div[@class='_2kHMtA'])[1]//span)[9]")
review = review_element.text
print(review)

# Close the WebDriver
driver.quit()