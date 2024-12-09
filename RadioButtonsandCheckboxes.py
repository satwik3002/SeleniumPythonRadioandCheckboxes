from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the LetsKodeIt practice URL in Chrome
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# Step 2: Wait for the page to load
time.sleep(5)

# Select BMW Radio Button
bmw_radio_button = driver.find_element(By.ID, "bmwradio")
bmw_radio_button.click()
time.sleep(2)

# Select Benz Radio Button
benz_radio_button = driver.find_element(By.ID, "benzradio")
benz_radio_button.click()
time.sleep(2)

# Select BMW Checkbox
bmw_checkbox = driver.find_element(By.ID, "bmwcheck")
bmw_checkbox.click()
time.sleep(2)

# Select Benz Checkbox
benz_checkbox = driver.find_element(By.ID, "benzcheck")
benz_checkbox.click()
time.sleep(2)

# Print the selection status of radio buttons and checkboxes
print("BMW Radio button is selected? " + str(bmw_radio_button.is_selected()))
print("Benz Radio button is selected? " + str(benz_radio_button.is_selected()))
print("BMW Checkbox is selected? " + str(bmw_checkbox.is_selected()))
print("Benz Checkbox is selected? " + str(benz_checkbox.is_selected()))

# Count the number of radio buttons and checkboxes
radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and not(ancestor::div[contains(@style,'display:none')])]")

print(f"Number of radio buttons: {len(radio_buttons)}")
print(f"Number of checkboxes: {len(checkboxes)}")

# Close the browser
driver.quit()
