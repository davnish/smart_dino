from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import cv2 as cv
import numpy as np
import time
from PIL import ImageGrab
import matplotlib.pyplot as plt

class WebDino:
    def __init__(self):
        
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(50,200)
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
        self.state = self.returnState()
        self.stateClip()
        self.rescaleState()
        # self.addTimeStamp()
        self.expandim()
        return self.state

    def step(self, action):
        self.timeStamp += 1
        self.takeAction(action)
        # time.sleep(0.001)
        self.state = self.returnState()
        self.terminated = self.isTerminated()
        reward = self.stateReward()
        self.stateClip()
        self.rescaleState()
        # self.addTimeStamp()
        self.expandim()
        return self.state, reward, self.terminated
    
    def takeAction(self, action):
        if action == 1: self.element.send_keys(Keys.SPACE)

    def returnState(self):
        # self.element.screenshot('dino.png') 
        state = ImageGrab.grab(bbox = (50, 340, 650, 576)).convert('L')
        # if self.timeStamp == 0:
        #     state.show()
        # state = cv.imread('dino.png', cv.IMREAD_GRAYSCALE)
        state = cv.Canny(np.asarray(state), 100, 200)
        return state.astype('float32')
    
    def isTerminated(self):
        return self.driver.execute_script("return Runner.instance_.crashed")
    
    def stateClip(self):
        self.state = self.state[41:160, 27:320]
    
    def addTimeStamp(self):
        timeStamp = np.zeros((23, 1)).astype('float32')
        timeStamp[0,0] = self.timeStamp
        self.state = np.concatenate([self.state, timeStamp], axis = -1)
    
    def expandim(self):
        self.state = np.expand_dims(self.state, axis = 0)
    
    def stateReward(self):
        reward = 0
        if self.terminated: reward -= -10
        reward += 1
        return reward
    
    def rescaleState(self, rescale_factor = 0.5):

        width = int(self.state.shape[1]*rescale_factor)
        height = int(self.state.shape[0]*rescale_factor)
        dimensions = (width, height)
        self.state = cv.resize(self.state, dimensions, interpolation=cv.INTER_AREA)
    
    def Simulate(self, games=3):
        for _ in range(games):
            currState = self.reset()
            terminated = False
            while not terminated:
                action = np.random.choice(self.action_space)
                currState, reward, terminated = self.step(action)
                ###############
                # if not terminated:
                plt.imshow(np.int32(currState.transpose(1,2,0)), cmap='grey')
                plt.axis('off')
                plt.savefig(f'misc/trans_inv/dino_{self.timeStamp}', bbox_inches = 'tight', pad_inches = 0) 
                ###############
                # plt.show()
                # print(currState.shape)
                # break 
            print(f"Score: {self.timeStamp}")
            break
        self.driver.quit()

if __name__ == "__main__":
    dino = WebDino()
    dino.Simulate(games = 10)
