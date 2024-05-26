img = cv.imread('over/over_16.png', cv.IMREAD_GRAYSCALE).astype('float32')
threshold, img_thresh = cv.threshold(img, 100, 255, cv.THRESH_BINARY)