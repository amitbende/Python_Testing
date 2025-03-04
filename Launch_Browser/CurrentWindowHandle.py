import time
from selenium import webdriver

# ChromeDriver Execution
options = webdriver.ChromeOptions()

# If path is true
options.add_experimental_option("detach", True)

# Object of chrome driver
driver = webdriver.Chrome(options=options)

# Open FaceBook
driver.get("https://www.facebook.com/")

# Current window handle
S1 = driver.current_window_handle
print(S1)

# Implicitly wait for 2 seconds
time.sleep(2)

# Close the browser gracefully
driver.quit()
