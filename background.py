import pygame
from random import random, randint

backgrounds = [
"pygames-underwater/1_game_background.png", 
"pygames-underwater/2_game_background.png",
"pygames-underwater/3_game_background.png",
"pygames-underwater/4_game_background.png"]




class Background:
    def __init__(self):
        self.x = 0,
        self.y = 0
        self.width = 900
        self.height = 500
        self.start = None
        self.image = None
        self.random()

    def random(self):
        self.start = randint(0,3)
        self.image = backgrounds[self.start]

    def rotate(self):
        if self.start == 3:
            self.start = 0
            self.image = backgrounds[self.start]
        else: 
            self.start += 1
            self.image = backgrounds[self.start]

    def load(self):
        self.image = pygame.image.load(self.image)
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (900, 500))

    