import pygame 
pygame.init()
from random import random, randint
from gameobject import GameObject
from junk import Junk
from treasure import Treasure
from player import Player
from bomb import Bomb
from background import Background
from scoreboard import ScoreBoard


# Set the game window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_height, screen_height])

#select a background
background = Background()
background.random()
background.load()

#set the scoreboard
score = ScoreBoard(30, 30, 0, 'score')
high_score = ScoreBoard(330, 30, 0, 'high score')

#create initial game elements
junk1 = Junk()
junk2 = Junk()
junk3 = Junk()
treasure1 = Treasure()
treasure2 = Treasure()
treasure3 = Treasure()
treasure4 = Treasure()
bomb = Bomb()
player = Player()

junks = [junk1, junk2, junk3]
treasures = [treasure1, treasure2, treasure3, treasure4]

# Make a group
all_sprites = pygame.sprite.Group()
junk_sprites = pygame.sprite.Group()
treasure_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(bomb)
all_sprites.add(score)

for junk in junks:
    all_sprites.add(junk)
    junk_sprites.add(junk)

for treasure in treasures:
    all_sprites.add(treasure)
    treasure_sprites.add(treasure)

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

    high_score.render(screen)
    # # # Check Colisions
    junk = pygame.sprite.spritecollideany(player, junk_sprites)
    if junk:
        score.sub(randint(1,3))
        junk.reset()

    # # # Check Colisions
    treasure = pygame.sprite.spritecollideany(player, treasure_sprites)
    if treasure:
        score.add(randint(3,5))
        treasure.reset()

    # # # Check collision player and bomb
    bomb_collide = pygame.sprite.collide_rect(player, bomb)
    if bomb_collide:
        print('Bomb Collide')
        print(bomb.rect)
        print(player.rect)
        if score.score > high_score.score: 
            print('new high score')
            high_score.sub(high_score.score)
            high_score.add(score.score)

        #reset game
        background.rotate()
        background.load()
        for treasure in treasures:
            treasure.dx = (randint(0, 200) / 100) + 1
        for junk in junks:
            junk.dy = (randint(0, 200) / 100) + 1
        for entity in all_sprites:
            entity.reset()
    
    # Get the clock
    clock = pygame.time.Clock()

    #----------------------------------------------------------


    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)



