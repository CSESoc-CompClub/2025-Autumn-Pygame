# Task 0
import pygame
pygame.init()

# Task 1.1
screen_size_x = 800
screen_size_y = 600
screen = pygame.display.set_mode((screen_size_x, screen_size_y))

# Task 1.3
background = pygame.image.load("images/background/wooden_floor.jpeg")
background = pygame.transform.scale(background, (screen_size_x, screen_size_y))
screen.blit(background, (0, 0))

# Task 1.4
pygame.display.set_caption("My game")
pygame.display.set_icon(pygame.image.load("images/game_icon.png"))

# Task 2.1 - create player class
class Player:
    def __init__(self):
        self.sprite = "images/player/poco_down.png"
        self.position_x = 0
        self.position_y = 0
        self.player_size = (100, 100)
        
    # Task 2.3 - create draw method
    def draw(self):
        player = pygame.image.load(self.sprite)
        player = pygame.transform.scale(player, self.player_size)
        screen.blit(player, (self.position_x, self.position_y))
    
    # Task 2.4 - create move method
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position_y -= 5
            
        elif keys[pygame.K_a]:
            self.position_x -= 5
            
        elif keys[pygame.K_s]:
            self.position_y += 5
            
        elif keys[pygame.K_d]:
            self.position_x += 5
    

# Task 2.2 - create a player instance and print out the properties
player = Player()
print(player.sprite, player.position_x, player.position_y, player.player_size)

# Task 2.3 - draw the player
player.draw()

# Task 1.2 - create a running loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    # Task 2.5 - fix the poco LOL
    screen.blit(background, (0, 0))
    
    # Task 2.4 - getting the player to move
    player.move()
    player.draw()

    pygame.display.update()