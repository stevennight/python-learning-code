import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, main):
        super().__init__()

        self.settings = main.settings
        self.screen = main.screen
        self.ship = main.ship

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = self.ship.rect.midright

        self.x = self.rect.x

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)