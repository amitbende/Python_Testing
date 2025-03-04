from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get("https://www.ilovepdf.com/word_to_pdf")
driver.maximize_window()

# Wait
driver.implicitly_wait(10)

# Click "Select Pdf file"
select_file_button = driver.find_element(By.XPATH, "//*[@id='pickfiles']")
select_file_button.click()

# Step-I: Copy PDF file(Ctrl + C)/Copy to Clipboard
file_path = "C:\\Users\\HP\\Desktop\\SDET\\Automation Testing\\Java\\Logical Programs.docx"
input_field = driver.find_element(By.TAG_NAME, "input")  # Find the input field for file upload
input_field.send_keys(file_path)

# Step-II: Press "ENTER" key
input_field.send_keys(Keys.RETURN)

# Wait for the file to upload (you can adjust the wait time if needed)
time.sleep(3)

# Click the "Convert" button
convert_button = driver.find_element(By.XPATH, "//button[@id='processTask']")
convert_button.click()

# Wait for the conversion to finish (you can adjust the wait time if needed)
time.sleep(3)

# Quit the browser
driver.quit()
