from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from PIL import Image
import numpy as np
import time

class WebDino:
    def __init__(self):
        
        self.driver = webdriver.Chrome()
        try: self.driver.get("chrome://dino/")
        except WebDriverException: pass

        #---------- Needs exp
        # self.driver.fullscreen_window()
        # time.sleep(1)
        #---------- 

        self.element = self.driver.find_element(By.TAG_NAME, 'body')
        # self.observation_space = 
        self.action_space = 3
        # self.actions = ActionChains(self.driver)

    def train(self):
        # self.takeAction()
        # time.sleep(1)
        # print(self.step(self.action_space.sample()))
        # self.takeAction()
        # time.sleep(1)
        # print(self.step())
        for ep in range(3):
            self.takeAction(1)
            time.sleep(2)

            terminated = False
            while not terminated:
                action = np.random.choice(self.action_space)
                currState, terminated = self.step(action)
                print(terminated)

        self.driver.quit()

    def step(self, action):
        self.takeAction(action)
        time.sleep(1)
        state = self.returnState()
        return state, self.isTerminated(state)
        # time.sleep(1)
    
    def takeAction(self, action):
        # print(action)
        if action == 1: self.element.send_keys(Keys.SPACE)
        elif action == 2: self.element.send_keys(Keys.ARROW_UP)

    def returnState(self):
        self.element.screenshot('dino.png') 
        state = np.asarray(Image.open('dino.png'))
        return state
    
    def isTerminated(self, state):
        # print(state)
        isOver_1 = np.sum([state[578, 347], state[583, 342], state[589, 336], state[596, 329]])
        over_1 = 2052
        isOver_2 = np.sum([state[564, 334], state[573, 337], state[591, 336], state[608, 338]])
        over_2 = 2100
        print(isOver_1, isOver_2)
        if isOver_1 == over_1 or isOver_2 == over_2:
            return True
        else: return False


if __name__ == "__main__":
    dino = WebDino()
    dino.train()