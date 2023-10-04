import pygame.image


class Ship:
    def __init__(self, main):
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()

        self.ship = pygame.image.load('images/ship.bmp')
        self.rect = self.ship.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.y = self.rect.y
        self.x = self.rect.x
        self.move_top = False
        self.move_bottom = False
        self.move_left = False
        self.move_right = False

    def update(self):
        if self.move_top and self.y > 0:
            self.y -= self.settings.ship_speed
        if self.move_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.move_left and self.x > 0:
            self.x -= self.settings.ship_speed
        if self.move_right and self.rect.right < self.screen_rect.right / 2:
            self.x += self.settings.ship_speed

        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.ship, self.rect)