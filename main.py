import pygame
import random
import math
from value import *
import mapFunc
import player

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title
pygame.display.set_caption('Space Invaders')

# initialize
mapInfo = mapFunc.mapFunc(screen)
player = player.player(screen)



# Game Loop
running = True
ang=0
move=0
while running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    mapInfo.drawMinimap()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ang=-0.8
            if event.key == pygame.K_RIGHT:
                ang=+0.8
            if event.key == pygame.K_UP:
                move=0.3

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                ang=0
            if event.key == pygame.K_UP:
                move=0
            
    #pos = player.checkPos()
    #if ((pos).x<=0.00 or (pos).x>=MINI_MAP_WIDTH*MINI_MAP_PIXEL or (pos).y<=0.00 or (pos).y>=MINI_MAP_HEIGHT*MINI_MAP_PIXEL):
    #    player.moveF(-0.05)
    #else:
    #    move=abs(move)
    player.changeAng(ang)
    player.moveF(move)
    player.drawMinimapPlayer()

    pygame.display.update()
