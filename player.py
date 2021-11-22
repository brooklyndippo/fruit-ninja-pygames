from gameobject import GameObject

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(250, 250, 'player.png')
        self.dx = 250 - 32
        self.dy = 250 - 32
        self.x = 250
        self.y = 250
        print ('Player Reset')
        self.reset()

    def left(self):
        if self.dx >= 125:
            self.dx -= 125

    def right(self):
        if self.dx < 343:
            self.dx += 125

#58 x 64
    def up(self):
        if self.dy >= 125:
            self.dy -= 125

    def down(self):
        if self.dy < 343:
            self.dy += 125

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32
