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

# Set Window size
S1 = driver.set_window_rect(x=100, y=200, width=1024, height=700)
print(S1)

# Implicitly wait for 2 seconds
time.sleep(2)

# Close the browser gracefully
driver.quit()
