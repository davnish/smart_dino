from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
import time
driver = webdriver.Chrome()

driver.get('https://chromedino.com/')
    # driver.get(game_url)


# Launch the browser

# Open a webpage
# time.sleep(10)
# Find an input field
# driver.implicitly_wait(10)
# Simulate key press events

# input_field.send_keys("Aur kajal kya haal chal hain!")  # Type "Hello" into the input field
# time.sleep(2)  # Wait for 2 seconds

actions = ActionChains(driver)
actions.send_keys(Keys.SPACE)
actions.perform() 
time.sleep(3)
actions = ActionChains(driver)
actions.send_keys(Keys.SPACE)
actions.perform() 
# time.sleep(5)
# actions.send_keys(Keys.SPACE)
# actions.send_keys(Keys.SPACE)

time.sleep(8)
input_field = driver.find_element(By.CLASS_NAME, 'runner-canvas')  # Replace "input_field_id" with the actual ID of the input field
input_field.screenshot('dino.png')
# input_field.send_keys(Keys.SPACE)

# input_field.send_keys(Keys.SPACE)  # Press the Enter key
# input_field.send_keys(Keys.SPACE)  # Press the Enter key

# Close the browser
driver.quit()
