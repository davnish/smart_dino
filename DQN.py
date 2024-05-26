import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import flatten
from collections import deque
import numpy as np
import pandas as pd
import random
import time
import os
random.seed(42)
torch.manual_seed(42)

class createNetwork(nn.Module):
    def __init__(self):
        super(createNetwork,self).__init__()
        self.conv1 = nn.Conv2d(1,8, kernel_size=(3,3))   
        self.maxpool1 = nn.MaxPool2d(3) 
        
        self.conv2 = nn.Conv2d(8,16, kernel_size=(3,3))    
        self.maxpool2 = nn.MaxPool2d(3)
                
        self.conv3 = nn.Conv2d(16, 32, kernel_size=(3,3)) 
        self.maxpool3 = nn.MaxPool2d(3)

        self.flat = nn.Flatten()
        self.l1 = nn.Linear(1248, 512)
        self.output = nn.Linear(512, 2)
    
    def forward(self, x):

        x = F.relu(self.conv1(x))
        x = self.maxpool1(x)

        x = F.relu(self.conv2(x))
        x = self.maxpool2(x)

        x = F.relu(self.conv3(x))
        x = self.maxpool3(x)

        x = self.flat(x)
        x = F.relu(self.l1(x))
        x = self.output(x)
        return x


class DeepQLearning:
    def __init__(self, env, gamma, epsilon, epsilon_decay, epsilon_end, lr, TAU, replayBufferSize, batchReplayBufferSize, numberEpisodes, load_model = True):
        '''
        env : This is the environment.
        gamma : Discount Factor.
        epsilon : Probability of choosing the random action.
        epsilon_decay : The rate of decay of epsilon.
        epsilon_end : The lowest you want the epsilon to be.
        lr : Learning rate of the online network.
        TAU : Soft Updating parameter of the target network.
        replayBufferBufferSize : The size of replay buffer.
        batchReplayBufferSize : The size of the sampled replay buffer to train the online network.
        numberEpisodes : No of episodes to be trained on.
        '''
        self.env=env
        self.gamma=gamma 
        self.epsilon=epsilon 
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
        self.lr = lr
        self.TAU = TAU 
        self.actionDimension = env.action_space # total no of action
        self.numberEpisodes=numberEpisodes
        self.replayBufferSize = replayBufferSize
        self.batchReplayBufferSize = batchReplayBufferSize
        self.replayBuffer=deque(maxlen=self.replayBufferSize)
        self.sumRewardsEpisode = [] # A list of rewards of every episodes

        # self.device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu' # If You want to use gpu uncommnet this
        self.device = 'cpu'
        self.onlineNetwork = createNetwork().to(self.device)
        self.targetNetwork = createNetwork().to(self.device)
        if load_model == True:
            self.onlineNetwork.load_state_dict(torch.load('models/DQ_1.pt')) # Setting the weights of online network -> target network 

        self.targetNetwork.load_state_dict(self.onlineNetwork.state_dict()) # Setting the weights of online network -> target network 

        self.loss_fn = nn.MSELoss()
        self.optimizer = torch.optim.AdamW(self.onlineNetwork.parameters(), lr = self.lr) # Adding weight decay
    
    def trainigEpisodes(self):

        for indexEpisode in range(self.numberEpisodes):

            rewardsEpisode = 0
            currState = torch.tensor(self.env.reset()) # Converting to tensor
            terminated = False
            while not terminated: # A timeStamp restriciton is for any episode taking more than 1000 states
                currAction = self.selectAction(currState.unsqueeze(0), indexEpisode)
                nxtState, reward, terminated = self.env.step(currAction)
                nxtState = torch.tensor(nxtState)
                self.replayBuffer.append((currState, currAction, reward, nxtState, terminated)) # Converting the nxtState to tensor
                self.trainNetwork()
                currState = nxtState
                rewardsEpisode += reward

                # Soft updating the target and online network
                online_net_state_dict = self.onlineNetwork.state_dict()
                target_net_state_dict = self.targetNetwork.state_dict()
                for key in online_net_state_dict:
                    target_net_state_dict[key] = online_net_state_dict[key]*self.TAU + target_net_state_dict[key]*(1-self.TAU)
                self.targetNetwork.load_state_dict(target_net_state_dict)

            print(f"Episode: {indexEpisode}, Reward: {rewardsEpisode}")
            self.sumRewardsEpisode.append(rewardsEpisode)

            self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)
  
    def selectAction(self, currState, indexEpisode):
        if torch.rand(1).item() < self.epsilon:
            return np.random.choice(self.env.action_space)
        else:
            with torch.no_grad():
                q_value = self.onlineNetwork(currState.to(self.device))
                # print(q_value)
                return torch.argmax(q_value).item()
        
    def trainNetwork(self):

        if(len(self.replayBuffer) > self.batchReplayBufferSize):
            batch = list(zip(*random.sample(self.replayBuffer, self.batchReplayBufferSize)))

            currStates = torch.stack(batch[0]).to(self.device)
            actions = torch.LongTensor(batch[1]).unsqueeze(1).to(self.device)
            rewards = torch.FloatTensor(batch[2]).unsqueeze(1).to(self.device)
            nxtStates = torch.stack(batch[3]).to(self.device)
            is_terminated = torch.BoolTensor(batch[4]).unsqueeze(1).to(self.device)
            
            with torch.no_grad():
                max_next_q_values = self.targetNetwork(nxtStates).max(-1, keepdims = True)[0]
                target_q_values = rewards + (self.gamma * max_next_q_values * ~is_terminated)    
            
            self.onlineNetwork.train()        
            self.optimizer.zero_grad()
            q_value = self.onlineNetwork(currStates).gather(1, actions)
            loss = self.loss_fn(q_value.squeeze(), target_q_values.squeeze())
            loss.backward()
            self.optimizer.step()

    def simulateStrategy(self, env):
        self.onlineNetwork.eval()
        env = env
        state = env.reset()
        self.onlineNetwork.eval()
        for _ in range(1000):
            with torch.no_grad():
                action = torch.argmax(self.onlineNetwork(torch.tensor(state, dtype=torch.float32).to(self.device).unsqueeze(0))).item() # Selecting here the best optimal strategy
            state, _, terminated = self.env.step(action)
            time.sleep(0.05)
            if terminated:
                time.sleep(1)
                break

    def plotRewards(self, model_no, avg_intv = 100):
        rwds = np.asarray(self.sumRewardsEpisode)
        score = np.sum((rwds>=200))
        hg_score = np.sum(rwds>=300)
        print(f"Ep Solved : {score}, High_Score : {hg_score}")

        solved = np.ones(self.numberEpisodes) * 200
        # avg_rwds = np.mean(rwds.reshape(-1, avg_intv), axis = -1, keepdims=True).repeat(avg_intv, axis = 1).reshape(-1)
        # rwds_df = pd.DataFrame({'Rewards': rwds, 'Average_Rewards': avg_rwds, 'Solved': solved})
        rwds_df = pd.DataFrame({'Rewards': rwds, 'Solved': solved})

        # plt.figure(figsize=(10, 10))
        plt.plot(rwds_df['Rewards'], color='blue', linewidth=2, label = 'Rewards')
        # plt.plot(rwds_df['Average_Rewards'], color='orange', linestyle='dashed',linewidth=2, label = f'Avg_Rewards')
        plt.plot(rwds_df['Solved'], color='red', linestyle='dashed', linewidth=1, label = 'Solved')
        plt.legend()
        plt.xlabel('Episode')
        plt.ylabel('Reward')
        # plt.yscale('log') 
        plt.savefig(os.path.join('results', f'DQ_{model_no}'))
        plt.show()

if __name__ == "__main__":
    x = torch.rand(1,1,119,384)
    model = createNetwork()
    st = time.time()
    x = model(x)
    ed = time.time()
    print(ed-st)
    print(x.size())
