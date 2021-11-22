import pygame 
pygame.init()
from random import random, randint
from gameobject import GameObject
from apple import Apple
from strawberry import Strawberry
from player import Player
from bomb import Bomb
from background import Background

# Set the game window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_height, screen_height])

background = Background()
background.random()
background.load()

apple = Apple()
apple2 = Apple()
apple3 = Apple()
strawberry = Strawberry()
strawberry2 = Strawberry()
strawberry3 = Strawberry()
bomb = Bomb()
player = Player()

apples = [apple, apple2, apple3]
strawberries = [strawberry, strawberry2, strawberry3]
fruits = [apple, apple2, apple3, strawberry, strawberry2, strawberry3]

# Make a group
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(bomb)

for fruit in fruits:
    all_sprites.add(fruit)
    fruit_sprites.add(fruit)

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
    screen.blit(background.image, [0, 0])


    #----------------------------------------------------------
    # #YOUR DRAWING
    

    # Move and render Sprites (Player and FRUITS)
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

        # # # Check Colisions
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()

    # # # Check collision player and bomb
    bomb_collide = pygame.sprite.collide_rect(player, bomb)
    if bomb_collide:
        print('Bomb Collide')
        print(bomb.rect)
        print(player.rect)
        #reset game
        background.rotate()
        background.load()
        for strawberry in strawberries:
            strawberry.dx = (randint(0, 200) / 100) + 1
        for apple in apples:
            apple.dy = (randint(0, 200) / 100) + 1
        for entity in all_sprites:
            entity.reset()
    
    # Get the clock
    clock = pygame.time.Clock()

    #----------------------------------------------------------


    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)



