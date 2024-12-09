from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Replace with webdriver.Firefox() or webdriver.Edge() for other browsers

# Step 1: Launch the Facebook Registration URL
driver.get("https://www.facebook.com/campaign/landing.php")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

# Step 2: Interact with the Gender Radio Buttons
# Select Female Radio Button
female_button = driver.find_element(By.XPATH, "//input[@value='1']")  # 'value=1' corresponds to Female
female_button.click()
print("Female radio button selected.")
time.sleep(2)

# Select Male Radio Button
male_button = driver.find_element(By.XPATH, "//input[@value='2']")  # 'value=2' corresponds to Male
male_button.click()
print("Male radio button selected.")
time.sleep(2)

# Select Custom Radio Button
custom_button = driver.find_element(By.XPATH, "//input[@value='-1']")  # 'value=-1' corresponds to Custom
custom_button.click()
print("Custom radio button selected.")
time.sleep(2)

# Close the browser
driver.quit()
