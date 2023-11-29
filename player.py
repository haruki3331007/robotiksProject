## *player.py
## This file contains:
## *Player class

import pygame
import mathFunc
from value import MINI_MAP_PIXEL

class player:
    def __init__(self, screen):
        self.mapP = MINI_MAP_PIXEL
        self.screen = screen
        self.pos = pygame.math.Vector3(self.mapP*10, self.mapP*10, 0) # first position
        self.ang = 0
        self.mathFunc = mathFunc.playerMathFunc(self)

    def drawMinimapPlayer(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.pos.x, self.pos.y), self.mapP/1.5)
        view = self.pos + pygame.math.Vector3(50, 0, 0).rotate_z(self.ang-30)
        pygame.draw.line(self.screen, (0, 255, 0), (self.pos.x, self.pos.y), (view.x, view.y), width=1) #y coordinate of player (Green)
        view = self.pos + pygame.math.Vector3(50, 0, 0).rotate_z(self.ang)
        pygame.draw.line(self.screen, (255, 0, 0), (self.pos.x, self.pos.y), (view.x, view.y), width=1) #x coordinate of player (Red)
        view = self.pos + pygame.math.Vector3(50, 0, 0).rotate_z(self.ang+30)
        pygame.draw.line(self.screen, (0, 255, 0), (self.pos.x, self.pos.y), (view.x, view.y), width=1) #y coordinate of player (Green)

        self.mathFunc.worldCoordinateSystem()
    
    def changeAng(self, ang):
        self.ang+=ang

    def moveF(self, move):
        self.pos = self.pos + pygame.math.Vector3(move, 0, 0).rotate_z(self.ang)
    
    def checkPos(self):
        return self.pos
    
    def checkAng(self):
        return self.ang

