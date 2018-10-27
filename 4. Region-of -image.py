import cv2
import numpy as np

img = cv2.imread('Images/im3.jpg',cv2.IMREAD_COLOR)

px = img[55,55]  # extracting a pixel value
print(px)

'''

ROI : region of image
it is basically is subimage of an image

'''
roi = img[150:500, 200:600 ] # extracting region of image in roi
img[0:350, 0:400] = roi # writing back to image but in other place

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()