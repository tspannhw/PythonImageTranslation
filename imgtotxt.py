import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('image.jpg',0)

######HERE IS WHERE TO DO THINGS
## source, minval,maxval, size of sobel kernal(default 3), L2 gradient(specifies equation for magniture{default false})

edges = cv2.Canny(img,100,200)

kernel = np.ones((5,5), np.uint8)

fat = cv2.dilate(edges,kernel,iterations = 5) 


######SHOW THE IMAGE
cv2.imshow('image',edges)
#destroy window on keypress
cv2.waitKey(0)
cv2.destroyAllWindows()



######SHOW THE IMAGE
cv2.imshow('image',img)
#destroy window on keypress
cv2.waitKey(0)
cv2.destroyAllWindows()


y=1
x=1

##Get size of image
size = img.shape

height = size[1]
width = size[0]

rezx=256
rezy=256


##magic will happen


f = open("walls.txt", "w")
while x < width:
	while y < height:
		xy = edges[x, y]
		if xy != 0:
			f.write("(hx == " + str(x+((rezx-width)/2)) + ") & (hy == " + str(y+((rezy-height)/2)) + ") | ")
			
		y += 1
		
		#print str(x) + "/" + str(width)
		
	
	x += 1
	y=0
f.close()

x=0
y=0
print 'done'
			






#####SAVE THE IMAGE
cv2.imwrite('output.jpg',edges)
