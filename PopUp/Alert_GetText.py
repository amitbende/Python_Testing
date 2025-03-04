import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://demo.guru99.com/test/delete_customer.php")

driver.find_element(By.NAME, "cusid").send_keys("amitbende")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)

# Switch to Alert pop-up and OK Button
Text = driver.switch_to.alert.text
print(Text)

driver.quit()