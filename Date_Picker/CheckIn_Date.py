from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://www.booking.com/")

time.sleep(2)

# Click Close button
driver.find_element(By.XPATH, "//button[@class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e f4552b6561']").click()

# Click CheckIn Date Calendar
driver.find_element(By.XPATH, "//button[@class='d47738b911 e246f833f7 fe211c0731']").click()

# Step-I: Declare 2 Variables -> (1) Month and Year (2) Date
Expected_MonthYear = "August 2023"
Expected_Date = "28"

while True:
    Actual_Month_Year = driver.find_element(By.XPATH, "//h3[@class='ead010d0b7 caf094216b e37cfa350e']").text
    print(Actual_Month_Year)

    if Expected_MonthYear == Actual_Month_Year:
        break
    else:
        driver.find_element(By.XPATH, "//button[@class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 f671049264 deab83296e f4552b6561 dc72a8413c f073249358']").click()

# Get all the dates
All_dates = driver.find_elements(By.XPATH, "(//table[@class='eb03f3f27f'])[1]//tr/td")
print(All_dates)
for date in All_dates:
    ActualDate = date.text

    if Expected_Date == ActualDate:
        date.click()
        break

# Quit the browser
# driver.quit()
