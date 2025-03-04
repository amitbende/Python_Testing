from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# ChromeDriver Execution
options = webdriver.ChromeOptions()

# If path is true
options.add_experimental_option("detach", True)

# Object of chrome driver
driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://www.facebook.com/")

time.sleep(2)

create_account_link = driver.find_element(By.XPATH, "//a[text()='Create new account']")
create_account_link.click()

time.sleep(2)

month_dropdown = driver.find_element(By.ID, "month")

actions = ActionChains(driver)

actions.click(month_dropdown).perform()

time.sleep(2)

# To move upward
actions.send_keys(Keys.ARROW_UP).perform()  # Jul
actions.send_keys(Keys.ARROW_UP).perform()  # Jun
actions.send_keys(Keys.ARROW_UP).perform()  # May
actions.send_keys(Keys.ARROW_UP).perform()  # April

time.sleep(2)

# To select the option
actions.send_keys(Keys.ENTER).perform()  # April

time.sleep(2)  # Adjust the wait time as needed

driver.quit()