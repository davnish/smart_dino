from PIL import ImageGrab
from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt

# for _ in range(9):
#     ss = ImageGrab.grab(bbox=(0, 400, 1300, 700))
#     ss.save("ss.png")
#     print(np.array(ss))
#     time.sleep(1)
# ss.close()

img = Image.open('over_1.png').convert('RGB')
img = np.array(img)
# print(img.shape)
# print(img.shape[0]//2, img.shape[1]//2)q
# print(np.array(img)[:,:2])
# img.show()
def isTerminated(state):
    # print(state)
    isOver_1 = np.sum([state[:, 117, 447], state[:, 111, 452], state[:, 104, 458], state[: ,96, 465]])
    over_1 = 1032
    print(isOver_1)
    isOver_2 = np.sum([state[:, 104, 432], state[:, 104, 442], state[:, 104, 460], state[: ,104, 477]])
    over_2 = 1080
    print(isOver_2)
    if isOver_1 == over_1 or isOver_2 == over_2:
        return True
    else: return False

img = np.transpose(img[232:432, 132:], (2,0,1))
print(img.shape)
print(isTerminated(img))

plt.imshow(img.transpose((1,2,0)))
plt.show()


