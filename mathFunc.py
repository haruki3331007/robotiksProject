# mathFunc.py
## This file contains:
## * math functions

import pygame
import numpy as np
from value import * 

class mapMathFun:
    def __init__(self, map):
        self.map = map
        self.mapW = MAP_WIDTH
        self.mapH = MAP_HEIGHT

    # scaring matrix to minimap size
    def minimapConverter(self):
        mapP = MINI_MAP_PIXEL
        minimap = np.array(self.map)
        minimap = minimap.repeat(mapP, axis=0).repeat(mapP, axis=1)
        return minimap
    
    def worldCoordinateSystem(self):
        # local : x --> right, y --> bottom, z --> depth
        # world : x --> right, y --> depth,  z --> up
        # so Rotation matrix is Rx(pi/2)

        self.worldmap = [[(self.map[j][i]).rotate_x(90) for i in range(self.mapW)] for j in range(self.mapH)]
        self.worldmap = np.array(self.worldmap)
        self.worldmap = self.worldmap.repeat(WORLD_MAP_PIXEL, axis=0).repeat(WORLD_MAP_PIXEL, axis=1).repeat(WORLD_MAP_PIXEL, axis=2)


    def viewCoordinateSystem(self, camera):
        # camera position = player position
        #
        return 0



class playerMathFunc:
    def __init__(self, player):
        self.player = player
        self.playerPos = self.player.checkPos()
        self.playerAng = self.player.checkAng()
    
    def worldCoordinateSystem(self):
        #set player to center of player positon in world map 
        self.worldPos = pygame.math.Vector3(self.playerPos.x + WORLD_MAP_PIXEL/2, self.playerPos.y + WORLD_MAP_PIXEL/2, 0) # first position
        self.worldPos  = self.worldPos.rotate_x(90)