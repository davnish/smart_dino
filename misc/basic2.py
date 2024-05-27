import numpy as np

# n = 5

arr = np.random.rand(1,2,3)

n = np.zeros((1,2,1))
n[0,0,0] = 5
print(n)
arr = np.concatenate([arr, n], axis = -1)
print(arr)
# print(n.shape)
# print(arr.shape)
# arr = np.concatenate([arr, n], axis = 2)
# print(n)
# print(arr)
