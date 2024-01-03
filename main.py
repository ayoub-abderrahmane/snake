import pygame,sys,random
from pygame.math import Vector2


class SNAKE:
    # Dessiner trois carré cote a cote
    def __init__(self):
        self.body =  self.body = [Vector2(5, 8), Vector2(4, 8), Vector2(3, 8)]
        self.direction = Vector2(1,0)
        self.new_block = False    
    def draw_snake(self):
        # Creer un rectangle
        # Dessiner un rectangle
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)

    def move_snake(self):
        if self.new_block == True:
             body_copy = self.body[:]
             body_copy.insert(0,body_copy[0] + self.direction)
             self.body = body_copy[:]
             self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

       
    
    def add_block(self):
        self.new_block = True
        
class FRUIT:
    def __init__(self):
        # Créer x et y
        # Dessiner un carré a un endroit random
        self.randomize()
    def draw_fruit(self):
        # Dessiner le carré
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size ,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
    def randomize(self):
        self.x = random.randint(0,cell_number -1) 
        self.y = random.randint(0,cell_number -1) 
        self.pos = Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        # Recréer un fruit lorsque la tete en mange un
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    
    def game_over(self):
        pygame.quit()
        sys.exit()
    
pygame.init()
cell_size = 40
cell_number = 16
screen = pygame.display.set_mode((cell_number * cell_size ,cell_number * cell_size))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Timer pour mettre le serpent en mouvement
        if event.type == SCREEN_UPDATE:
            main_game.update()
        # Pour diriger le serpent avec les touches
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
