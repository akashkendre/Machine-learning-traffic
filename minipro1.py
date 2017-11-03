import numpy as np
import cv2
import traffic

img1 = cv2.imread('test2.jpg')
h,w,c = img1.shape
print img1.shape
count=0


gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
j = 125
for i in range(0,9):
    px = thresh1[125,j]
    j=j+70
    print px
    if(px==255):
       count=count+1
if(count<=5):
    print("Timing changed")
    traffic.orange(1)
    traffic.green(8)
    traffic.red(12)
else:
    print("Timing not changed")
    traffic.orange(1)
    traffic.green(4)
    traffic.red(12)
cv2.imshow('OriginalImage',img1)
cv2.imshow('ThresholdedImage',thresh1)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
