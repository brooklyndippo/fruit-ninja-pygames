from gameobject import GameObject
from random import random, randint
import pygame


class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'pygames-underwater/PNG/Bonus/Small-bomb.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = (randint(0, 200) / 100) + 1
        self.reset() 

    def move(self):
        if self.direction == 'right':
            self.x += self.dx
            # Check the x position of the bomb
            if self.x > 500: 
                self.reset()
        elif self.direction == 'left':
            self.x -= self.dx
            # Check the y position of the bomb
            if self.x < -50: 
                self.reset()
        elif self.direction == 'down':
            self.y += self.dy
            # Check the y position of the bomb
            if self.y > 500: 
                self.reset()
        elif self.direction == 'up':
            self.y -= self.dy
            # Check the y position of the bomn
            if self.y < -50: 
                self.reset()

    #when it goes offscreen replace it
    def reset(self):
        lane = [93, 218, 343]
        self.x = lane[randint(0,2)]
        self.y = lane[randint(0,2)]

        direction = ['left', 'right', 'up', 'down']
        self.direction = direction[randint(0,3)]

        if self.direction == 'left':
            self.x = 550

        elif self.direction == 'right':
            self.x = -50
        
        elif self.direction == 'up':
            self.y = 550

        elif self.direction == 'down':
            self.y = -50

        print('bomb:')
        print(self.direction)
