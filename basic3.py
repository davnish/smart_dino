from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the Chrome Dino game
driver.get("chrome://dino")

# Wait for the game to load
time.sleep(2)

# Send space key to start the game
body = driver.find_element_by_tag_name("body")
body.send_keys(Keys.SPACE)

# Wait for the game to start
time.sleep(1)

# Check if the game over message is displayed
game_over_message = driver.find_element_by_id("offline-resources-1x").text
if "Game over" in game_over_message:
    print("Game over")
else:
    print("Game still running")

# Close the WebDriver
driver.quit()
