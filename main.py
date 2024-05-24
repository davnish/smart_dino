from env import WebDino
from DQ_train import DeepQLearning
import torch
import time
import os


if __name__ == "__main__":

    # Explanation of every hyperparameter is in the docstirng of `DeepQLearning` class
    # Hyperparameters ###########
    model_no = 3
    numberEpisodes = 1000
    gamma = 0.99
    epsilon = 1
    epsilon_decay = 0.992 # changing this from 0.995
    epsilon_end = 0.1 # Changing this from 0.05
    lr = 1e-4
    TAU = 0.001
    replayBufferSize = 10000
    batchReplayBufferSize = 256
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
    dqn.simulateStrategy()
    dqn.plotRewards(model_no, avg_intv=4)