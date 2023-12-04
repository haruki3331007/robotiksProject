## *player.py
## This file contains:
## *Player class

import pygame
import numpy as np
from value import MAP_WIDTH, MAP_HEIGHT

class player:
    def __init__(self, screen):
        self.screen = screen
        self.pos = pygame.math.Vector3(5*10, 5*10, 0) # first position
        self.ang = 0

    def drawMinimapPlayer(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.pos.x, self.pos.y), 1)
        view = self.pos + pygame.math.Vector3(8, 0, 0).rotate_z(self.ang-30)
        pygame.draw.line(self.screen, (0, 255, 0), (self.pos.x, self.pos.y), (view.x, view.y), width=1) #coordinate of player (Green)
        view = self.pos + pygame.math.Vector3(8, 0, 0).rotate_z(self.ang)
        pygame.draw.line(self.screen, (255, 0, 0), (self.pos.x, self.pos.y), (view.x, view.y), width=1) #coordinate of player (Red)
        view = self.pos + pygame.math.Vector3(8, 0, 0).rotate_z(self.ang+30)
        pygame.draw.line(self.screen, (0, 255, 0), (self.pos.x, self.pos.y), (view.x, view.y), width=1) #coordinate of player (Green)

    
    def changeAng(self, ang):
        self.ang+=ang

    def moveF(self, move):
        self.pos = self.pos + pygame.math.Vector3(move, 0, 0).rotate_z(self.ang)
    
    def checkPos(self):
        return self.pos
    
    def checkAng(self):
        return self.ang
    

    def vecCheck(self, mapW):
        vecTop = pygame.math.Vector3(self.pos.x-8, self.pos.y-8, self.pos.z)

        for i in range(int(self.pos.y)-8, int(self.pos.y)+8):
            for j in range(int(self.pos.x)-8, int(self.pos.x)+8):
                if 0<j<MAP_WIDTH and 0<i<MAP_HEIGHT:
                    if mapW[i][j].z == 1:
                        pygame.draw.circle(self.screen, (255, 0, 0), (j, i), 1)
                        O = pygame.math.Vector3(self.pos.x, self.pos.y, 0)
                        A = O + pygame.math.Vector3(8, 0, 0).rotate_z(self.ang-30)
                        B = O + pygame.math.Vector3(8, 0, 0).rotate_z(self.ang+30)
                        P = pygame.math.Vector3(j, i, 0)

                        vecA = A-O
                        vecB = B-O
                        vecP = P-O

                        vecA = np.array([vecA.x, vecA.y])
                        vecB = np.array([vecB.x, vecB.y])
                        vecP = np.array([vecP.x, vecP.y])

                        # inner product
                        AP = np.dot(vecA, vecP)
                        BP = np.dot(vecB, vecP)

                        if(AP>0 and BP>0):
                            print(AP, BP)
                            pygame.draw.circle(self.screen, (255, 0, 0), (j, i), 2)

    def playerPosCheck(self):
        font = pygame.font.Font(None, 55)
        text = font.render("(X, Y) = (" + str(int(self.pos.x)) + ", " + str(int(self.pos.y)) + ")", True, (255,255,255))
        self.screen.blit(text, [400, 350])

    def worldCoordinateSystem(self):
        #set player to center of player positon in world map 
        self.worldPos = pygame.math.Vector3(self.pos.x + 5/2, self.pos.y + 5/2, 200) # first position
        self.worldPos  = self.worldPos.rotate_x(90)

