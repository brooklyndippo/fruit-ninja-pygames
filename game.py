import pygame 
pygame.init()
from gameobject import GameObject
from apple import Apple
from strawberry import Strawberry
from player import Player

# Set the game window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_height, screen_height])


apple = Apple()
apple2 = Apple()
apple3 = Apple()
strawberry = Strawberry()
strawberry2 = Strawberry()
strawberry3 = Strawberry()
player = Player()

fruits = [apple, apple2, apple3, strawberry, strawberry2, strawberry3]

# Make a group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

for fruit in fruits:
    all_sprites.add(fruit)

print(all_sprites)

# Create the GAME LOOP ------------------------------------------
running = True 
while running: 
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for event type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
  
	# Looks at events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))

    #----------------------------------------------------------
    # #YOUR DRAWING
 

    # Move and render Sprites (Player and FRUITS)
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    
    # Get the clock
    clock = pygame.time.Clock()

    #----------------------------------------------------------


    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)



