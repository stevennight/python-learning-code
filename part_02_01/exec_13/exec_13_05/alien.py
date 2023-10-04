import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, main):
        super().__init__()
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = main.screen.get_rect()

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.x = 0
        self.y = 0

    def update(self):
        self.x -= self.settings.alien_speed

        self.rect.x = self.x
        self.rect.y = self.y