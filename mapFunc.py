## mapFunc.py
## This file contains:
## *map information

import random
import pygame
from value import *
import mathFunc 

class mapFunc:
    def __init__(self, screen):
        self.mapW = MAP_WIDTH
        self.mapH = MAP_HEIGHT
        self.screen = screen
        self.mapP = MINI_MAP_PIXEL

        self.map = [[pygame.math.Vector3(i, j, 0) for i in range(self.mapW)] for j in range(self.mapH)] #oridinal map

        for i in range(self.mapH):                             #map assign enemies
            rndNum = random.randint(0, 5)
            for j in range(rndNum):
                rndPos = random.randint(0, self.mapW-1)
                self.map[i][rndPos].z = 1

        self.mathFunc = mathFunc.mapMathFun(self.map)
        self.minimap = self.mathFunc.minimapConverter()

    def drawMinimap(self):
        pygame.draw.rect(self.screen, (255,255,255), (0,0,self.mapW*self.mapP,self.mapH*self.mapP))
        for i in range(self.mapH*self.mapP):
            for j in range(self.mapW*self.mapP):
                atr = self.minimap[i][j]
                if atr[2]==1:
                    self.screen.fill((101,101,101),((j, i), (1, 1)))
    
    def worldmap(self):
        self.worldmap = self.mathFunc.worldCoordinateSystem()

