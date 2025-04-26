# Task 1
import pygame
pygame.init()

# Task 2.1
screen_size_x = 800
screen_size_y = 600
screen = pygame.display.set_mode((screen_size_x, screen_size_y))

# Task 2.3
background_image = "images/background/wooden_floor.jpeg"
background = pygame.transform.scale(pygame.image.load(background_image), (screen_size_x, screen_size_y))
screen.blit(background, (0, 0))

# Task 2.4
pygame.display.set_caption("My game")
pygame.display.set_icon(pygame.image.load("images/game_icon.png"))

# Task 3.1 - create player class
class Player:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.size = (100, 100)
        self.image = "images/player/poco_down.png"
        self.sprite = pygame.transform.scale(pygame.image.load(self.image), self.size)
        # Task 5.1 - create hitbox and make sure it updates
        self.hitbox = self.sprite.get_rect().move(self.position_x, self.position_y)
        # Task 6.1 - create a score
        self.score = 0
    
    # Task 5.1 - create hitbox and make sure it updates
    def update(self):
        self.hitbox = self.sprite.get_rect().move(self.position_x, self.position_y)
    
    # Task 3.3 - create draw method
    def draw(self):
        screen.blit(self.sprite, (self.position_x, self.position_y))
    
    # Task 3.4 - create move method
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position_y -= 1
            # Task 3.6 - bonus task: make poco turn when moving
            self.image = "images/player/poco_up.png"

        if keys[pygame.K_a]:
            self.position_x -= 1
            # Task 3.6 - bonus task: make poco turn when moving
            self.image = "images/player/poco_left.png"

        if keys[pygame.K_s]:
            self.position_y += 1
            # Task 3.6 - bonus task: make poco turn when moving
            self.image = "images/player/poco_down.png"

        if keys[pygame.K_d]:
            self.position_x += 1
            # Task 3.6 - bonus task: make poco turn when moving
            self.image = "images/player/poco_right.png"
    
    # Task 5.2 - colliding with the fruit removes it from active fruits
    def interact_foods(self, food):
        collision = self.hitbox.colliderect(food.hitbox)
        if collision:
            active_foods.remove(food)
            # Task 6.2 - increase the score if foods have been picked up
            player.score += 1
                

# Task 3.2 - create a player instance and print out the properties
player = Player()
print(player.sprite, player.position_x, player.position_y, player.size)

# Task 3.3 - draw the player
player.draw()

# Task 4.1 - create a food class
class Food:
    def __init__(self, name, image, position_x, position_y):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.size = (50, 50)
        self.image = image
        self.sprite = pygame.transform.scale(pygame.image.load(image), self.size)
        # Task 5.1 - create hitbox and make sure it updates
        self.hitbox = self.sprite.get_rect().move(self.position_x, self.position_y)
    
    # Task 4.4 - create a draw method inside food
    def draw(self):
        screen.blit(self.sprite, (self.position_x, self.position_y))
        
# Task 4.2 - create a food dictionary
foods = {
    # "food" : ["sprite path", pos_x, pos_y]
    # key : value
    "banana": ["images/food/banana.png", 300, 500],
    "grapes": ["images/food/grapes.png", 500, 400],
    "peach": ["images/food/peach.png", 200, 400],
    "strawberry": ["images/food/strawberry.png", 300, 100],
    "sushi": ["images/food/sushi.png", 600, 200],
    "watermelon": ["images/food/watermelon.png", 100, 400]
}

# Task 4.3 - initialise active foods
active_foods = []
for key, value in foods.items():
    # key is the food name and the value[0] is sprite, value[1] is pos_x
    # value[2] is pos_y
    print(key, value[0], value[1], value[2])
    active_foods.append(Food(key,value[0], value[1], value[2]))

# Task 6.3 - show the score on the screen
font = pygame.font.SysFont('Palatino', 50)
font_colour = (255, 255, 255) # pygame colours use RGB values, this value is white
score_pos = (10, 10)

# Task 2.2 - create a running loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    # Task 3.5 - fix the duplicating poco LOL
    screen.blit(background, (0, 0))
    
    # Task 3.4 - getting the player to move
    player.move()
    player.draw()
    
    # Task 5.1 - update the player hitbox
    player.update()
    
    # Task 4.5 - show all the foods in the active food list
    for foods in active_foods:
        player.interact_foods(foods)
        foods.draw()
        
    # Task 6.3 - show the score on the screen
    score_text = font.render(f'Score: {player.score}', True, font_colour)
    screen.blit(score_text, score_pos)
    if (player.score == 6): # game over! you win :)
        print("You win!")
        running = False
    

    pygame.display.update()