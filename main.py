from env import WebDino
from DQN import DeepQLearning
import pandas as pd
import torch
import time
import os
import glob


if __name__ == "__main__":

    # Explanation of every hyperparameter is in the docstirng of `DeepQLearning` class
    # Hyperparameters ###########
    model_no = 4
    numberEpisodes = 1000
    gamma = 0.99
    epsilon = 1
    epsilon_decay = 0.995 # Changing this from 0.995
    epsilon_end = 0.05 # Changing this from 0.05
    lr = 1e-4
    TAU = 0.001
    replayBufferSize = 10000
    batchReplayBufferSize = 32
    save_freq = 100
    #############################

    env = WebDino()
    # env.action_space.seed(42)

    dqn = DeepQLearning(env, gamma=gamma, epsilon=epsilon, epsilon_decay=epsilon_decay, 
                        epsilon_end=epsilon_end, lr = lr, replayBufferSize=replayBufferSize, 
                        batchReplayBufferSize=batchReplayBufferSize, TAU=TAU, numberEpisodes=numberEpisodes, model_no=model_no, save_freq = save_freq)
    start = time.time()
    dqn.trainigEpisodes()
    end = time.time()
    print(f'Time: {end - start}')
    torch.save(dqn.onlineNetwork.state_dict(), os.path.join('models', f'DQ_{model_no}', f'ckpt_{numberEpisodes}.pt')) # Saving the model
    dqn.plotRewards(model_no, avg_intv=4)