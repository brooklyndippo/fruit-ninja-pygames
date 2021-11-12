from gameobject import GameObject
from random import random, randint


class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset() 

    #initialize movement
    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Check the y position of the apple
        if self.x > 500: 
            self.reset()

    #when it goes offscreen replace it
    def reset(self):
        lane = [93, 218, 343]
        self.x = randint(-100, -64)
        self.y = lane[randint(0,2)]


