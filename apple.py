from gameobject import GameObject
from random import random, randint

junk = [
    "pygames-underwater/PNG/Let/Anchor.png",
    "pygames-underwater/PNG/Let/Steering-wheel.png",
    "pygames-underwater/PNG/Let/Barrel_2.png"
]


class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, junk[randint(0,2)])
        self.dy = (randint(0, 200) / 100) + 1
        self.reset() 

    #initialize movement
    def move(self):
        if self.direction == 'down':
            self.y += self.dy
            # Check the y position of the apple
            if self.y > 500: 
                self.reset()
        elif self.direction == 'up':
            self.y -= self.dy
            # Check the y position of the apple
            if self.y < -50: 
                self.reset()

    #when it goes offscreen replace it
    def reset(self):
        lane = [93, 218, 343]
        self.dy += .1
        self.x = lane[randint(0,2)]
        up_or_down = [-50, 550]
        self.y = up_or_down[randint(0,1)]
        if self.y == -50:
            self.direction = 'down'
        if self.y == 550:
            self.direction = 'up'
        print(self.direction)


