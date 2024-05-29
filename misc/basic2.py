import numpy as np
import torch


n = torch.rand(1,1,1)
print(n)
n = n.repeat(4,1,1)
print(n)
