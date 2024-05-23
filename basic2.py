from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Launch the browser
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://offline-dino-game.firebaseapp.com/")

# Find an input field
input_field = driver.find_element(By.CLASS_NAME,'runner-canvas')  # Replace "input_field_id" with the actual ID of the input field
# driver.implicitly_wait(10)
# Simulate key press events
input_field.send_keys("Aur kajal kya haal chal hain!")  # Type "Hello" into the input field

# time.sleep(2)  # Wait for 2 seconds
actions = ActionChains(driver)
actions.send_keys(Keys.SPACE)
actions.perform() 

# time.sleep(5)
# input_field.screenshot('dino.png')
actions.send_keys(Keys.SPACE)
# actions.send_keys(Keys.SPACE)
# actions.send_keys(Keys.SPACE)

time.sleep(10)

# input_field.send_keys(Keys.SPACE)  # Press the Enter key
# input_field.send_keys(Keys.SPACE)  # Press the Enter key
# Close the browser
driver.quit()
