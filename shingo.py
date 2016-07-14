#!/usr/bin/env python -u

#import everything
import numpy as np
import cv2
import os as os
from sailfish.geo import EqualSubdomainsGeometry2D
from sailfish.subdomain import Subdomain2D
from sailfish.node_type import NTFullBBWall, NTHalfBBWall
from sailfish.controller import LBSimulationController
from sailfish.lb_single import LBFluidSim
from sailfish.lb_base import LBForcedSim

# Load an color image in grayscale
img = cv2.imread('star.png',0)

##Gets the edges of the image
## source, minval,maxval, size of sobel kernal(default 3), L2 gradient(specifies equation for magniture{default false})
edges = cv2.Canny(img,100,200)
#scrapedges = cv2.Canny(img,100,200)

##thickens the image if neccisary
#kernel = np.ones((5,5), np.uint8)
#fat = cv2.dilate(edges,kernel,iterations = 5) 

y=1
x=1




#contours,hierarchy = cv2.findContours(scrapedges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)



#cnt = contours[0]
#print cnt
#x,y,w,h = cv2.boundingRect(cnt)



#crop = edges[y:y+h,x:x+w]


##Get size of image
size = edges.shape

height = size[1]
width = size[0]

rezx=width+100
rezy=height+200


##converts the image to numpy array coordinates for the simulation


f = open("walls.txt", "w")
print "open"
while y < height:
	while x < width:
		xy = edges[x, y]
		if xy != 0:
			f.write("(hx == " + str(x+((rezx-width)/2)) + ") & (hy == " + str(y+((rezy-height)/2)) + ") | ")
			
		x += 1
		
		#print str(x) + "/" + str(width)
		
	
	y += 1
	x=0
f.close()

x=0
y=0
print 'done'
			

#####SAVE THE IMAGE
cv2.imwrite('output.jpg',edges)

######SHOW THE IMAGE
#cv2.imshow('image',edges)
#destroy window on keypress
#cv2.waitKey(0)
#cv2.destroyAllWindows()


###################################################################SAILFISH####################################################

#opens numpy coordinates in readable format
for line in open("walls.txt"):
	readline = line[:-3]


class CylinderBlock(Subdomain2D):
    def boundary_conditions(self, hx, hy):
        wall_bc = NTFullBBWall
	walls = eval(readline)
	
	
	#creates the walls	
	self.set_node(walls, wall_bc)
      
        

    def initial_conditions(self, sim, hx, hy):
        sim.rho[:] = 1.0
        sim.vy[:] = 0.0
        sim.vx[:] = 0.0


class CylinderSimulation(LBFluidSim, LBForcedSim):
    subdomain = CylinderBlock

    @classmethod
    def update_defaults(cls, defaults):
        defaults.update({
		
            'lat_nx': rezx,
            'lat_ny': rezy,
            'visc': 0.1})


    @classmethod
    def add_options(cls, group, dim):
        group.add_argument('--vertical', action='store_true')

    @classmethod
    def modify_config(cls, config):
        if config.vertical:
            config.periodic_y = True
        else:
            config.periodic_x = True

    def __init__(self, config):
        super(CylinderSimulation, self).__init__(config)

        if config.vertical:
            self.add_body_force((0.0, 1e-5))
        else:
            self.add_body_force((1e-5, 0.0))


if __name__ == '__main__':
    ctrl = LBSimulationController(CylinderSimulation, EqualSubdomainsGeometry2D)
    ctrl.run()


