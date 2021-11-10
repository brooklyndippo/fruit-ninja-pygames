import pygame 
pygame.init()
from gameobject import GameObject

# Set the game window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_height, screen_height])


apple = GameObject(0, 250, 'apple.png')

# Create the game loop ------------------------------------------
running = True 
while running: 
	# Looks at events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))

    #----------------------------------------------------------
    # #YOUR DRAWING
    
    # class GameObject(pygame.sprite.Sprite):
    #     def __init__(self, x, y, image):
    #         super(GameObject, self).__init__()
    #         self.surf = pygame.image.load(image)
    #         self.x = x
    #         self.y = y

    #     def render(self, screen):
    #         screen.blit(self.surf, (self.x, self.y))

    
    # Get the clock
    clock = pygame.time.Clock()
    

    # Make an instance of GameObject

    apple.x += 1
    apple.render(screen)


    
    # Make an instance of GameObject



#   # #draw the fruits
    for num in range (0,9):
        x = num % 3
        y = int(num/3)

        if num % 2:
            fruit = 'strawberry.png'

        else:
            fruit = 'apple.png'

        newFruit = GameObject (((x+1)*100), ((y+1)*100), fruit)
        newFruit.render(screen)
#     #----------------------------------------------------------


    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)



