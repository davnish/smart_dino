import gymnasium as gym
from DQN import createNetwork
import torch
from gymnasium import RewardWrapper
import numpy as np

class TranformReward(RewardWrapper):
    def __init__(self, env: gym.Env, f):
        super().__init__(env)
        # self.reward_range = [0,2]
        self.f = f
        self.env = env

    def reward(self, reward: np.float32) -> np.float32:
        return self.f(self.env)

def f(env):
    state = env.state[0]
    if -1 < state < 1 :
        return 1
    else: return -2

env = gym.make('CartPole-v1', render_mode = 'human')
currState = env.reset()[0]
env = TranformReward(env, f)
env.render()
onNet = createNetwork(4,2)
onNet.load_state_dict(torch.load("models/DQ_7.pt"))
print(currState[0])

terminate = False
while not terminate:
# for _ in range(1000):
    action = torch.argmax(onNet(torch.tensor(currState))).item()
    # action = np.random.choice(2)
    nxtState, reward, terminate, _, _ = env.step(action)
    print(nxtState[0], reward)
    currState = nxtState


    
