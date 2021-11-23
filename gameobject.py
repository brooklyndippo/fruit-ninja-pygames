import pygame 
pygame.init()
pygame.font.init()


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.image = pygame.image.load(image)
        self.width = 64
        self.height = 64
        self.load()

        self.surf = self.image
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()
        self.load()

    def load(self):
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))
    