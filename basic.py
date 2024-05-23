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

img = Image.open('dino.png')
img = np.array(img)
print(img.shape)
print(img.shape[0]//2, img.shape[1]//2)
# print(np.array(img)[:,:2])
# img.show()
import matplotlib.pyplot as plt
def isTerminated(state):
    # print(state)
    isOver_1 = np.sum([state[578, 347], state[583, 342], state[589, 336], state[596, 329]])
    print(state[578, 347], state[583, 342], state[589, 336], state[596, 329])
    over_1 = 1424
    isOver_2 = np.sum([state[564, 334], state[573, 337], state[591, 336], state[608, 338]])
    print([state[564, 334], state[573, 337], state[591, 336], state[608, 338]])
    over_2 = 1424
    print(isOver_1, isOver_2)
    if isOver_1 == over_1 or isOver_2 == over_2:
        return True
    else: return False

print(isTerminated(img))
plt.imshow(img)
plt.show()


