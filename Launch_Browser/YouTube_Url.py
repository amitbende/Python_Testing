import time
from selenium import webdriver

# ChromeDriver Execution
options = webdriver.ChromeOptions()

# If path is true
options.add_experimental_option("detach", True)

# Object of chrome driver
driver = webdriver.Chrome(options=options)

# Maximize Window Browser
driver.maximize_window()

# Open FaceBook
driver.get("https://www.youtube.com/")

# Implicitly wait for 5 seconds
time.sleep(5)

# Close the browser gracefully
driver.quit()
