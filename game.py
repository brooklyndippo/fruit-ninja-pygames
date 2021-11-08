import pygame 
pygame.init()

# Set the game window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_height, screen_height])

# Creat the game loop
running = True 
while running: 
	# Looks at events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #clear the screen
    screen.fill((255, 255, 255))

    #----------------------------------------------------------
    #YOUR DRAWING
	# Draw a circle
    
    color = (110, 110, 110)
    for x in range(1,4):
        part = screen_width/4
        x_value = part * x
            
        for y in range (1,4):
            part = screen_height/4
            y_value = part * y
            position = (x_value, y_value)
            pygame.draw.circle(screen, color, position, 50)


	#pygame.draw.circle(screen, color, position, 50)

    #----------------------------------------------------------


	# Update the display
    pygame.display.flip()
