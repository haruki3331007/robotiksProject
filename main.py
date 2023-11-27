import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption('Space Invaders')


# Game Loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # playerX += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Score
    font = pygame.font.SysFont(None, 32) # フォントの作成　Noneはデフォルトのfreesansbold.ttf
    score = font.render("Score : ", True, (255,255,255)) # テキストを描画したSurfaceの作成
    screen.blit(score, (20,50))
    pygame.display.update()
