import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('over/over_16.png', cv.IMREAD_GRAYSCALE).astype('float32')
threshold, img_thresh = cv.threshold(img, 100, 255, cv.THRESH_BINARY)

print(img.shape)
cx = img.shape[0] // 2
cy = img.shape[1] // 2
print(cx, cy)

# Draw a white circle with a radius of 20 pixels
# cv.circle(img_thresh, (323, 70), radius=1, color=(0), thickness=-1)

# Thresholding


def isTerminated(state):
    if state[70, 323] + state[73, 345] + state[70, 368] + state[74, 400] == 1020:
        return True
    else: return False

print(isTerminated(img_thresh))
plt.imshow(img_thresh, cmap='gray')
plt.show()
