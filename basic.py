from PIL import ImageGrab
import numpy as np
import time

for _ in range(9):
    ss = ImageGrab.grab(bbox=(0, 400, 1300, 700))
    ss.save("ss.png")
    print(np.array(ss))
    time.sleep(1)
ss.close()


