from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class WebAgent:
    def __init__(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get("https://chromedino.com/")
        self.element = self.driver.find_element(By.CLASS_NAME, 'runner-canvas')
        self.actions = ActionChains(self.driver)

    def currState(self):
        self.element.screenshot('dino.jpg')

    def train(self):
        self.takeActions()
        time.sleep(2)
        self.takeActions()
        time.sleep(5)
        self.currState()
        self.driver.quit()
    
    def takeActions(self):

        self.actions.send_keys(Keys.SPACE).perform()

if __name__ == "__main__":

    dino = WebAgent()
    dino.train()