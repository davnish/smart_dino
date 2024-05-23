from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
import time

class WebAgent:
    def __init__(self):
        
        self.driver = webdriver.Chrome()
        try: self.driver.get("chrome://dino/")
        except WebDriverException: pass
        
        #---------- Needs exp
        # self.driver.fullscreen_window()
        # time.sleep(1)
        #----------

        self.element = self.driver.find_element(By.TAG_NAME, 'body')
        # self.actions = ActionChains(self.driver)

    def currState(self):
        self.element.screenshot('dino.png')

    def train(self):
        self.takeActions()
        time.sleep(5)
        self.takeActions()
        time.sleep(5)
        self.currState()
        self.driver.quit()
    
    def takeActions(self):

        self.element.send_keys(Keys.SPACE)

if __name__ == "__main__":

    dino = WebAgent()
    dino.train()