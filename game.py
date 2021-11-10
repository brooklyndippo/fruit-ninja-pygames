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

    # Clear screen
    screen.fill((255, 255, 255))

    #----------------------------------------------------------
    #YOUR DRAWING
    
    class GameObject(pygame.sprite.Sprite):
        def __init__(self, x, y, image):
            super(GameObject, self).__init__()
            self.surf = pygame.image.load(image)
            self.x = x
            self.y = y

        def render(self, screen):
            screen.blit(self.surf, (self.x, self.y))

  # #draw the fruits
    for num in range (0,9):
        x = num % 3
        y = int(num/3)

        if num % 2:
            fruit = 'strawberry.png'

        else:
            fruit = 'apple.png'

        newFruit = GameObject (((x+1)*100), ((y+1)*100), fruit)
        newFruit.render(screen)
        print(x, y, fruit)

    #----------------------------------------------------------


	# Update the display
    pygame.display.flip()


