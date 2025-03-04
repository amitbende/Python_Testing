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

# Open Kite
driver.get("https://kite.zerodha.com/")

# Implicitly wait for 2 seconds
time.sleep(2)

# Back Browser
driver.back()

# Implicitly wait for 2 seconds
time.sleep(2)

# Forward Browser
driver.forward()

# Implicitly wait for 2 seconds
time.sleep(2)

# Browser Refresh
driver.refresh()

# Implicitly wait for 2 seconds
time.sleep(2)

# Close the browser gracefully
driver.quit()
