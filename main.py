import pygame
from value import *
import mapFunc
import player

# Initialize the pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')

# initialize the function
mapFunc = mapFunc.mapFunc(screen)
player = player.player(screen)

# Game Loop
running = True
ang=0
move=0
while running:
    # RGB = Red, Green, Blue
    pygame.draw.rect(screen, (135, 206, 235), (0, 0, SCREEN_WIDTH, 2*(SCREEN_HEIGHT/3)))
    pygame.draw.rect(screen, (49, 117, 70), (0, 2*(SCREEN_HEIGHT/3), SCREEN_WIDTH, SCREEN_HEIGHT))
    mapFunc.drawMinimap()

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

    player.vecCheck(mapFunc.mapCheck())
    player.playerPosCheck()

    pygame.display.update()
