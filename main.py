import pygame,sys,random
from pygame.math import Vector2

class SNAKE:
    # Dessiner trois carré cote a cote
    def __init__(self):
        self.body = [Vector2(5,8)],[Vector2(6,8)],[Vector2(7,8)]
    
    def draw_snake(self):
        # Creer un rectangle
        # Dessiner un rectangle
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos ,y_pos ,cell_size ,cell_size)
            pygame.draw.rect(screen,(183,191,122))

        


class FRUIT:
    def __init__(self):
        # Créer x et y
        # Dessiner un carré a un endroit random
        self.x = random.randint(0,cell_number -1) 
        self.y = random.randint(0,cell_number -1) 
        self.pos = Vector2(self.x,self.y)
    def draw_fruit(self):
        # Dessiner le carré
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size ,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
pygame.init()
cell_size = 40
cell_number = 16
screen = pygame.display.set_mode((cell_number * cell_size ,cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT ()
snake = SNAKE ()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)
