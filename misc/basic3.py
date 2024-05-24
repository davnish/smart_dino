from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By


import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the Chrome Dino game
try: driver.get("chrome://dino")
except WebDriverException: pass
driver.fullscreen_window()

# Wait for the game to load
time.sleep(2)

# Send space key to start the game
body = driver.find_element(By.TAG_NAME,"body")
body.send_keys(Keys.SPACE)

# Wait for the game to start
time.sleep(10)

# Check if the game over message is displayed
# game_over_text = driver.find_element(By.ID, "game_over").is_displayed()

# if game_over_text:
#     print("Game over")
# else:
#     print("Game still running")

# Close the WebDriver
driver.quit()
