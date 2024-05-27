from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
# from PIL import Image
import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt

class WebDino:
    def __init__(self):
        
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(600, 236)
        try: self.driver.get("chrome://dino")
        except WebDriverException: pass

        #---------- Needs exp
        # self.driver.fullscreen_window()
        # time.sleep(1)
        #---------- 

        self.element = self.driver.find_element(By.TAG_NAME, 'body')
        self.takeAction(1) # For Starting the inital game

        self.action_space = 2
    
    def reset(self):
        self.timeStamp = 0
        self.takeAction(1)
        time.sleep(3.5)
        state = self.stateClipUnsqueeze(self.returnState())
        return state

    def step(self, action):
        self.timeStamp += 1
        self.takeAction(action)
        time.sleep(0.001)
        state = self.returnState()
        terminated = self.isTerminated(state)
        reward = self.reward(terminated, action)
        stateClipped = self.stateClipUnsqueeze(state)
        return stateClipped, reward, terminated
    
    def takeAction(self, action):
        if action == 1: self.element.send_keys(Keys.SPACE)
        # elif action == 2: self.element.send_keys(Keys.ARROW_DOWN)

    def returnState(self):
        self.element.screenshot('dino.png') 
        state = cv.imread('dino.png', cv.IMREAD_GRAYSCALE).astype('float32')
        _, state = cv.threshold(state, 100, 255, cv.THRESH_BINARY)
        return state
    
    def isTerminated(self, state):
        if state[70, 323] + state[73, 345] + state[70, 368] + state[74, 400] == 1020:
            time.sleep(2)
            return True
        else: return False
    
    def stateClipUnsqueeze(self, state):
        state = np.expand_dims(state[41:160, 27:410], axis = 0)
        timeStamp = np.zeros((1, 119, 1))
        timeStamp[0,0,0] = self.timeStamp
        state = np.concatenate([state, timeStamp], axis = -1)
        return state
    
    def reward(self, terminated, action):
        reward = 0
        if terminated: reward -= -10
        reward += 1
        return reward
    
    def Simulate(self, games=3):
        for _ in range(games):
            currState = self.reset()
            terminated = False
            while not terminated:
                action = np.random.choice(self.action_space)
                currState, reward, terminated = self.step(action)
                if not terminated:
                    plt.imshow(np.int32(currState.transpose(1,2,0)))
                    plt.savefig(f'misc/img/dino_{self.timeStamp}') 
                # print(currState.shape)
                # break 
            # break
            print(f"Score: {self.timeStamp}")
        self.driver.quit()

if __name__ == "__main__":
    dino = WebDino()
    dino.Simulate(games = 10)

    #-----------------
    # Some issues with terminations are still to be resolved.