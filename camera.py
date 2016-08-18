import numpy as np
import cv2
# Load an color image in same format
img = cv2.imread('image.jpg',0)
height, width = img.shape[:2]



crop=img[(height/2)-128:(height/2)+128, (width/2)-128:(width/2)+128]

cv2.imwrite("image.jpg",crop)

######SHOW THE IMAGE
cv2.imshow('image',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
