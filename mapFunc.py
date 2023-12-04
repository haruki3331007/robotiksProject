## mapFunc.py
## This file contains:
## *map information

import random
import pygame
import random
import numpy as np
from value import *

class mapFunc:
    def __init__(self, screen):
        self.screen = screen

        self.mapW = MAP_WIDTH
        self.mapH = MAP_HEIGHT
        self.map = [[pygame.math.Vector3(i, j, 0) for i in range(self.mapW)] for j in range(self.mapH)] #oridinal map

        self.enemiesInit()

    #map assign enemies
    def enemiesInit(self):
        for i in range(self.mapH):
            rndNum = random.randint(0, 1)
            for _ in range(rndNum):
                rndPos = random.randint(0, self.mapW-1)
                self.map[i][rndPos].z = 1

    #map assign enemies
    def drawMinimap(self):
        pygame.draw.rect(self.screen, (255,255,255), (0,0,self.mapW,self.mapH))
        for i in range(self.mapH):
            for j in range(self.mapW):
                if self.map[i][j].z==1:
                    self.screen.fill((101,101,101),((j, i), (1, 1)))

    def mapCheck(self):
        return self.map

    def worldCoordinateSystem(self):
        # local : x --> right, y --> bottom, z --> depth
        # world : x --> right, y --> depth,  z --> up
        # so Rotation matrix is Rx(pi/2)

        self.worldmap = [[(self.map[j][i]).rotate_x(90) for i in range(self.mapW)] for j in range(self.mapH)]
        self.worldmap = np.array(self.worldmap)
        self.worldmap = self.worldmap.repeat(WORLD_MAP_PIXEL, axis=0).repeat(WORLD_MAP_PIXEL, axis=1).repeat(200, axis=2)    

