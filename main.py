import pygame
height = 900
width = 600
surf = pygame.display.set_mode((900,600))
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()