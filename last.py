#!/usr/bin/env python -u
"""
Simulates the flow around a 2D cylinder.

The flow is periodic and driven by a body force.
"""
rezx = 256
rezy = 256

import numpy as np
import os as os
from sailfish.geo import EqualSubdomainsGeometry2D
from sailfish.subdomain import Subdomain2D
from sailfish.node_type import NTFullBBWall, NTHalfBBWall
from sailfish.controller import LBSimulationController
from sailfish.lb_single import LBFluidSim
from sailfish.lb_base import LBForcedSim





path = os.path.join(os.path.expanduser('~'), 'IMAGE', 'walls.txt')
print path
for line in open(path):
	readline = line[:-3]


class CylinderBlock(Subdomain2D):
    def boundary_conditions(self, hx, hy):
        wall_bc = NTFullBBWall
	walls = eval(readline)
	#walls = (hx == 100) &  (hy < 300) | (hx == 160) &  (hy < 300)
	
	#print type(map)	
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
