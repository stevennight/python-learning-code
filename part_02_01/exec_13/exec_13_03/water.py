import pygame
from pygame.sprite import Sprite

class Water(Sprite):
    """雨滴"""
    def __init__(self, main):
        super().__init__()
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect

        self.rect = pygame.Rect(
            0, 0, self.settings.rain_width, self.settings.rain_height
        )
        self.x = 0
        self.y = 0

    def update(self):
        self.y += self.settings.rain_drop_speed
        self.rect.y = self.y

        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)