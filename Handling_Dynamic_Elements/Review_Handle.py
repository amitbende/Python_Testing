from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver for Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Maximize the browser window
driver.maximize_window()

# Open the URL
driver.get("https://www.flipkart.com/")

# Click on the initial popup if it exists
driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()

# Click on the first item in the list
driver.find_element(By.XPATH, "(//a[@class='_2KpZ6l _3dESVI'])[1]").click()

# Click on the first image of the selected item
driver.find_element(By.XPATH, "(//img[@class='_396cs4'])[1]").click()

# Close the WebDriver
driver.quit()
