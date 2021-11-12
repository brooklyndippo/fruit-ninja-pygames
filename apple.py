from gameobject import GameObject
from random import random, randint


class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset() 

    #initialize movement
    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Check the y position of the apple
        if self.y > 500: 
            self.reset()

    #when it goes offscreen replace it
    def reset(self):
        lane = [93, 218, 343]
        self.x = lane[randint(0,2)]
        self.y = randint(-100, -64)


