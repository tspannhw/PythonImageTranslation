import numpy as np
import cv2
# Load an color image in same format
img = cv2.imread('image.jpg',0)


######SHOW THE IMAGE
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
