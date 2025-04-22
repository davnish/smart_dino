from DQN import createNetwork
# import gymnasium as gym
# from gymnasium.utils.save_video import save_video
# from moviepy.editor import VideoFileClip
from env import WebDino
import torch
import time
import os
import glob
import numpy as np


def Simulate_DQ_Strategy(model_no, games = 6):
    # env = gym.make('LunarLander-v2', render_mode='human')
    env = WebDino()
    onlineNetwork = createNetwork()
    onlineNetwork.load_state_dict(torch.load(os.path.join('models', f"ckpt_{model_no}.pt")))
    onlineNetwork.eval()
    for _ in range(games):
        currState = env.reset()

        currState = torch.tensor(currState).repeat(4,1,1)

        rewards = 0
        terminated = False
        timeStamp = 0
        while not terminated:
            with torch.no_grad():
                action = torch.argmax(onlineNetwork(torch.tensor(currState).unsqueeze(0), )).item()
            time.sleep(0.09)
            nxtState, reward, terminated = env.step(action)
            nxtState = torch.tensor(nxtState)
            nxtState = torch.concat([nxtState, currState[:3]], dim = 0) # Concatinating 4 Consequetive images
            currState = nxtState

            rewards += reward
            timeStamp += 1
            if terminated or timeStamp>300:
                break
        print(f"Simulation Reward: {rewards}")

if __name__ == "__main__":
    # for model_no in range(1,6):
    #     saving_video(model_no, games = 1)
    # for _video in glob.glob(os.path.join('videos', '*.mp4')):
    #     video = VideoFileClip(_video)
    #     video.write_gif(os.path.join('results', f'{os.path.basename(_video).split('.')[0].split('-')[0]}.gif'),fps=10,program='imageio')
    # os.system('rm -rf videos')
    Simulate_DQ_Strategy(1800, games = 10)
    pass