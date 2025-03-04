from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--remote-allow-Origins=*")
options.add_argument("ignore-certificate-errors")

driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://www.flipkart.com/")

time.sleep(2)

email_input = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
email_input.send_keys("abc123@gmail.com")

time.sleep(2)

request_otp_button = driver.find_element(By.XPATH, "//button[text()='Request OTP']")
request_otp_button.click()

time.sleep(5)  # Adjust the wait time as needed

driver.quit()