import cv2 # imported the python-openCV module
import numpy # imported numpy

cap = cv2.VideoCapture(0) # this will capture the video from webcam
codec = cv2.VideoWriter_fourcc(*'XVID') # defining codec for writting video
out = cv2.VideoWriter('output.avi', codec, 30, (640,480)) 

while True: # infinite loop
    ret, frame = cap.read() # read the frame from the video, ret is true if video is captured
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert the captured video in gray
    out.write(gray)
    cv2.imshow('gray',gray) # show the gray image
    cv2.imshow('frame',frame) # show the original image
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # this is for breaking the infinite loop while 'q' is pressed
        break
cap.release() # release the captured frames so this can be used again
out.release() # release the writed frames
cv2.destroyAllWindows() # destroys the window

