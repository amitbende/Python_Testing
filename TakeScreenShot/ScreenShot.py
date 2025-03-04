from selenium import webdriver
import time
import os
import shutil

# Set up Chrome options with experimental option to detach
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Maximize the window
driver.maximize_window()

# Open the URL
driver.get("https://www.flipkart.com/")

# Wait for the page to load
time.sleep(2)

try:
    # Take a screenshot and save it as "screenshot.jpg"
    source_path = "screenshot.jpg"
    driver.save_screenshot(source_path)
    print(f"Screenshot saved: {source_path}")  # Print the screenshot path for verification

    # Specify the destination path
    destination_folder = "D:\\Amit  Software Testing\\AutoMation ScreenShots"
    destination_path = os.path.join(destination_folder, "flipCartss.jpg")
    print(f"Destination path: {destination_path}")  # Print the destination path for verification

    # Move the screenshot to the desired location
    # shutil.move(screenshot_path, destination_path)

    shutil.move(source_path, destination_path)
    print(f"Screenshot moved to destination path: {destination_path}")
except Exception as e:
    print("An error occurred while capturing or moving the screenshot:", str(e))
# with open(destination_path, 'wb') as fast:

# Quit the browser
driver.quit()