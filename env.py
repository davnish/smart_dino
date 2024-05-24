from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
        self.takeAction(1) # For Starting the inital game
        time.sleep(2)
        # self.observation_space = (3,200,1184)
        self.action_space = 2
    
    def reset(self):
        self.timeStamp = 0
        self.takeAction(1)
        time.sleep(3)
        state = self.returnState()
        return state

    def step(self, action):
        self.timeStamp += 1
        self.takeAction(action)
        # time.sleep(0.2)
        state = self.returnState()
        terminated = self.isTerminated(state)
        reward = self.reward()
        return state, reward, terminated
    
    def takeAction(self, action):
        # print(action)
        if action == 1: self.element.send_keys(Keys.SPACE)
        # elif action == 2: self.element.send_keys(Keys.ARROW_DOWN)

    def returnState(self):
        self.element.screenshot('dino.png') 
        state = self.stateClip(np.asarray(Image.open('dino.png').convert('RGB'), dtype=np.float32)).transpose((2,0,1))
        return state
    
    def isTerminated(self, state):
        isOver_1 = np.sum([state[:, 117, 447], state[:, 111, 452], state[:, 104, 458], state[: ,96, 465]])
        over_1 = 1032
        isOver_2 = np.sum([state[:, 104, 432], state[:, 104, 442], state[:, 104, 460], state[: ,104, 477]])
        over_2 = 1080
        if isOver_1 == over_1:
            time.sleep(1)
        if isOver_2 == over_2:
            time.sleep(1)
            return True
        else: return False
    
    def stateClip(self, state):
        return state[232:432, 132:]
    
    def reward(self):
        return 1
    
    def Simulate(self, games=3):
        for _ in range(games):
            currState = self.reset()
            terminated = False
            while not terminated:
                action = np.random.choice(self.action_space)
                currState, reward, terminated = self.step(action)

            print(f"Score: {self.timeStamp}")
        self.driver.quit()

if __name__ == "__main__":
    dino = WebDino()
    dino.Simulate()

    #-----------------
    # Some issues with terminations are still to be resolved.