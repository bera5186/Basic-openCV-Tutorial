import cv2 # importing the cv2 (python-openCV) module

img = cv2.imread('Images/im1.png') # reading the image in a matrix form
cv2.imshow('image',img) # showing the image, 1st arg: Window name, 2nd arg: Image matrix
cv2.waitKey(0) # waits for any key to be pressed
cv2.destroyAllWindows() # destroys the window
