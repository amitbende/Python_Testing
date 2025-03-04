import time
from selenium import webdriver

# ChromeDriver Execution
options = webdriver.ChromeOptions()

# If path is true
options.add_experimental_option("detach", True)

# Object of chrome driver
driver1 = webdriver.Chrome(options=options)
driver1.get("https://www.facebook.com/")
driver1.maximize_window()
time.sleep(3)
driver1.quit()

driver2 = webdriver.Chrome(options=options)
driver2.get("https://www.instagram.com/")
driver2.maximize_window()
time.sleep(3)
driver2.quit()

driver3 = webdriver.Chrome(options=options)
driver3.get("https://www.youtube.com/")
driver3.maximize_window()
time.sleep(3)
driver3.quit()

