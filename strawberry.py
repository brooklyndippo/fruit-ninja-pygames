from gameobject import GameObject
from random import random, randint


class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset() 

    def move(self):
        if self.direction == 'right':
            self.x += self.dx
            # Check the x position of the strawberry
            if self.x > 500: 
                self.reset()
        elif self.direction == 'left':
            self.x -= self.dx
            # Check the y position of the strawberry
            if self.x < -50: 
                self.reset()

    #when it goes offscreen replace it
    def reset(self):
        lane = [93, 218, 343]
        self.y = lane[randint(0,2)]
        left_or_right = [-50, 550]
        self.x = left_or_right[randint(0,1)]
        if self.x == -50:
            self.direction = 'right'
        if self.x == 550:
            self.direction = 'left'
        print(self.direction)
