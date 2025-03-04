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
driver.get("https://www.facebook.com/")

# set browser position
S1 = driver.set_window_position(900, 800, windowHandle='current')
print(S1)

# Implicitly wait for 2 seconds
time.sleep(5)

# Close the browser gracefully
driver.quit()
