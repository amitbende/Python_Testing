from selenium import webdriver
from selenium.webdriver.common.by import By

# ChromeDriver Execution
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("http://adactinhotelapp.com/HotelAppBuild2/index.php")

driver.find_element(By.ID, "username").send_keys("Velocity")    # Username
driver.find_element(By.ID, "password").send_keys("U1YP1G")      # PassWord
driver.find_element(By.ID, "login").click()                     # login Button

Expected_Username = "Velocity!"

UN = driver.find_element(By.ID, "username_show").get_attribute("value")
print(UN)

List = UN.split(" ")
print(List)

A1 = List[0]
print(A1)

Actual_Username = List[1]
print(Actual_Username)

if Expected_Username == Actual_Username:
    print("Test Case Pass!!")
else:
    print("Test Case Fail!!")
