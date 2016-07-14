#!/usr/bin/env python -u

#import everything
import numpy as np
import cv2
import os as os


# Load an color image in grayscale
img = cv2.imread('image.jpg',0)

##Gets the edges of the image
## source, minval,maxval, size of sobel kernal(default 3), L2 gradient(specifies equation for magniture{default false})
scrapedges = cv2.Canny(img,100,200)

##thickens the image if neccisary
#kernel = np.ones((5,5), np.uint8)
#fat = cv2.dilate(edges,kernel,iterations = 5) 

contours,hierarchy = cv2.findContours(scrapedges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)



cnt = contours[0]
print cnt
x,y,w,h = cv2.boundingRect(cnt)



crop = img[y:y+h,x:x+w]


cv2.imwrite('output.jpg',img)

######SHOW THE IMAGE
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


