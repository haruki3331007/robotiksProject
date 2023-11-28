## mapFunc.py
## This file contains:
## *map information

import random
import pygame
from value import *

class mapFunc:
    def __init__(self, screen):
        self.mapP = MINI_MAP_PIXEL
        self.mapW = MINI_MAP_WIDTH
        self.mapH = MINI_MAP_HEIGHT
        self.screen = screen

        self.worldmap = [[0 for column in range(self.mapW)] for row in range(self.mapH)]
        for i in range(self.mapH):
            rndNum = random.randint(0, 5)
            for j in range(rndNum):
                rndPos = random.randint(0, self.mapW-1)
                self.worldmap[i][rndPos] = 1

    def drawMinimap(self):
        pygame.draw.rect(self.screen, (255,255,255), (0,0,self.mapW*self.mapP,self.mapH*self.mapP))

        for i in range(self.mapH):
            for j in range(self.mapW):
                if self.worldmap[i][j]==1:
                    pygame.draw.rect(self.screen, (101,101,101), (j*self.mapP,i*self.mapP,self.mapP,self.mapP))

