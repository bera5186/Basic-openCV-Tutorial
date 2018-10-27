import cv2
import numpy

image = cv2.imread('/home/rahul/Programming/Computer-Vision/Images/im3.jpg', cv2.IMREAD_COLOR) # arg 1: absolute path of image, arg 2 : Mode of opening image

cv2.line(image, (0,0), (300,300), (0,100,200), 15) # arg 1: where to write, arg 2 : starting coordinate, arg 3: end coordiante, arg 4: color tuple (bgr), arg 5 : width of line 
cv2.rectangle(image, (0,0), (500,500), (0,150,0), 4,) # arg 1: where to write, arg 2 : starting coordinate, arg 3: end coordiante, arg 4: color tuple (bgr), arg 5 : width of line 
cv2.circle(image, (500,300), 100, (0,39,204), -1) # arg 1: where to write, arg 2: center of circle, arg 3: radius of circle, arg 4: color tuple, arg 5: line width (-1 fo fill)

pts = numpy.array([[10,5],[20,30],[50,10],[30,56],[23,68]], numpy.int32) # numpy array holding coordinates
cv2.polylines(image, [pts], True, (0,255,255), 2 ) # arg 1: where to write, arg 2: coordinates, arg 3: color tuple, arg 4: line width

font = cv2.FONT_HERSHEY_COMPLEX # defining cv2 font
cv2.putText(image, 'opencv', (1200,700), font, 5, (0,255,0), 2, cv2.LINE_AA) # arg 1: where to write , arg 2: what to write, arg 3: font, arg 4: size, arg 5: color tuple, arg 6: thickness, arg 7: line type

cv2.imshow('frame',image) # showing the image
cv2.waitKey(0) # wait for a key to be pressed for exiting
cv2.destroyAllWindows() # destroying frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, 'opencv', (100,200), font, 2, (0,255,0), 2, cv2.LINE_AA)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()