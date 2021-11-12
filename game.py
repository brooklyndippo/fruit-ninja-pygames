import pygame 
pygame.init()
from gameobject import GameObject
from apple import Apple
from strawberry import Strawberry

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

fruits = [apple, apple2, apple3, strawberry, strawberry2, strawberry3]

# Create the game loop ------------------------------------------
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
                print('LEFT')
            elif event.key == pygame.K_RIGHT:
                print('RIGHT')
            elif event.key == pygame.K_UP:
                print('UP')
            elif event.key == pygame.K_DOWN:
                print('DOWN')
  
	# Looks at events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))

    #----------------------------------------------------------
    # #YOUR DRAWING
    # Draw apple
    # apple.move()
    # apple.render(screen)
    # strawberry.move()
    # strawberry.render(screen)

    for fruit in fruits:
            fruit.move()
            fruit.render(screen)
    
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


    
    # Make an instance of GameObject



#   # #draw the fruits
    # for num in range (0,9):
    #     x = num % 3
    #     y = int(num/3)

    #     if num % 2:
    #         fruit = 'strawberry.png'

    #     else:
    #         fruit = 'apple.png'

    #     newFruit = GameObject (((x+1)*100), ((y+1)*100), fruit)
    #     newFruit.render(screen)
#     #----------------------------------------------------------


    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)



