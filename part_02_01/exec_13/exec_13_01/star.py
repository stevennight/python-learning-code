import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """星星"""

    def __init__(self, sky, rotate_degree=0):
        super().__init__()
        self.screen = sky.screen

        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.image, rotate_degree)
        # 将底色去除 230, 230, 230
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        self.x = 0
        self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y
