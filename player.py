## *player.py
## This file contains:
## *Player class

import pygame
from value import MINI_MAP_PIXEL

class player:
    def __init__(self, screen):
        self.mapP = MINI_MAP_PIXEL
        self.screen = screen
        self.pos = pygame.math.Vector2(self.mapP*10, self.mapP*10)
        self.ang = 0

    def drawPlayer(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.pos.x, self.pos.y), self.mapP/2 )
        view = self.pos + pygame.math.Vector2(20, 0).rotate(self.ang)
        pygame.draw.line(self.screen, (255, 0, 0), (self.pos.x, self.pos.y), (view.x, view.y), width=1) #x coordinate of player (Red)
        view = self.pos + pygame.math.Vector2(20, 0).rotate(self.ang+90)
        pygame.draw.line(self.screen, (0, 255, 0), (self.pos.x, self.pos.y), (view.x, view.y), width=1) #y coordinate of player (Green)
    
    def changeAng(self, ang):
        self.ang+=ang

    def moveF(self, move):
        self.pos = self.pos + pygame.math.Vector2(move, 0).rotate(self.ang)
    
    def checkPos(self):
        return self.pos

