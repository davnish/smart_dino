from env import WebDino
from DQN import DeepQLearning
import torch
import time
import os


if __name__ == "__main__":

    # Explanation of every hyperparameter is in the docstirng of `DeepQLearning` class
    # Hyperparameters ###########
    model_no = 3
    numberEpisodes = 1500
    gamma = 0.99
    epsilon = 1
    epsilon_decay = 0.995 # Changing this from 0.995
    epsilon_end = 0.05 # Changing this from 0.05
    lr = 1e-4
    TAU = 0.001
    replayBufferSize = 10000
    batchReplayBufferSize = 8
    #############################

    env = WebDino()
    # env.action_space.seed(42)

    dqn = DeepQLearning(env, gamma=gamma, epsilon=epsilon, epsilon_decay=epsilon_decay, 
                        epsilon_end=epsilon_end, lr = lr, replayBufferSize=replayBufferSize, 
                        batchReplayBufferSize=batchReplayBufferSize, TAU=TAU, numberEpisodes=numberEpisodes)
    start = time.time()
    dqn.trainigEpisodes()
    end = time.time()
    print(f'Time: {end - start}')
    torch.save(dqn.onlineNetwork.state_dict(), os.path.join('models', f'DQ_{model_no}.pt')) # Saving the model
    dqn.plotRewards(model_no, avg_intv=4)