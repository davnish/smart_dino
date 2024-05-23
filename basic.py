from PIL import ImageGrab
from PIL import Image
import numpy as np
import time

# for _ in range(9):
#     ss = ImageGrab.grab(bbox=(0, 400, 1300, 700))
#     ss.save("ss.png")
#     print(np.array(ss))
#     time.sleep(1)
# ss.close()

img = Image.open('over_2.png', )
img = np.array(img)
print(img.shape)
print(img.shape[0]//2, img.shape[1]//2)
# print(np.array(img)[:,:2])
# img.show()
import matplotlib.pyplot as plt
def isTerminated(state):
    # print(state)
    isOver_1 = np.sum([state[347, 578], state[342, 583], state[336, 589], state[329, 596]])
    over_1 = 2052
    isOver_2 = np.sum([state[334, 564], state[337, 573], state[336, 591], state[338, 608]])
    over_2 = 2100
    print(isOver_2)
    if isOver_1 == over_1 or isOver_2 == over_2:
        return True
    else: return False

print(isTerminated(img))
plt.imshow(img)
plt.show()


