from gameobject import GameObject
from random import random, randint

treasure = [
    "pygames-underwater/PNG/Bonus/Pearl.png",
    "pygames-underwater/PNG/Bonus/Coin.png",
    "pygames-underwater/PNG/Bonus/Acceleration.png",
    "pygames-underwater/PNG/Bonus/Crown.png"
]


class Treasure(GameObject):
    def __init__(self):
        super(Treasure, self).__init__(0, 0, treasure[randint(0,3)])
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset() 

    def move(self):
        if self.direction == 'right':
            self.x += self.dx
            # Check the x position of the treasure
            if self.x > 500: 
                self.reset()
        elif self.direction == 'left':
            self.x -= self.dx
            # Check the y position of the treasure
            if self.x < -50: 
                self.reset()

    #when it goes offscreen replace it
    def reset(self):
        lane = [93, 218, 343]
        self.y = lane[randint(0,2)]
        self.dx += .1
        left_or_right = [-50, 550]
        self.x = left_or_right[randint(0,1)]
        if self.x == -50:
            self.direction = 'right'
        if self.x == 550:
            self.direction = 'left'
        print(self.direction)
