from PIL import ImageGrab
from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt
import cv2 as cv


img = cv.imread('over/over_16.png', cv.IMREAD_GRAYSCALE).astype('float32')

print(img.shape)
cx = img.shape[0]//2
cy = img.shape[1]//2
cv.circle(img, (cx,cy), radius=50, color=255, thickness=-1)

# cv.imshow('img', img)
# cv.waitKey(0)s

print(np.unique(img, return_counts=True))
plt.imshow(img, cmap='gray')
plt.show()




