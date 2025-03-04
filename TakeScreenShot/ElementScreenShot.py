from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.flipkart.com/")

# Maximize the browser window
driver.maximize_window()

# Locate the element to capture a screenshot of (e.g., the first banner)
element_to_capture = driver.find_element(By.XPATH, "(//div[@class='_28p97w'])[1]")

# Use ActionChains to scroll into view
actions = ActionChains(driver)
actions.move_to_element(element_to_capture).perform()

# Capture a screenshot of the element
element_screenshot = element_to_capture.screenshot_as_png

# Specify the destination path for the screenshot
destination_path = "D:\\Amit Software Testing\\AutoMation ScreenShots\\Flip_login1.png"

# Save the element screenshot to the destination path
with open(destination_path, "wb") as file:
    file.write(element_screenshot)

print(f"Screenshot saved to destination path: {destination_path}")

# Quit the browser
driver.quit()