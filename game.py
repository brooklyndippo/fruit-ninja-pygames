import pygame 
pygame.init()

# Set the game window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_height, screen_height])

# Create a new instance of Surface
surface = pygame.Surface((50, 50))
surface.fill((255, 111, 33))

# Clear screen
screen.fill((255, 255, 255))

# Draw the surface
screen.blit(surface, (100, 120))


# Creat the game loop
running = True 
while running: 
	# Looks at events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #----------------------------------------------------------
    #YOUR DRAWING
    
    

    #----------------------------------------------------------


	# Update the display
    pygame.display.flip()
