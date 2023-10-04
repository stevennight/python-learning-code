import pygame.image


class Ship:
    def __init__(self, main):
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()

        self.ship = pygame.image.load('images/ship.bmp')
        self.ship_rect = self.ship.get_rect()
        self.ship_rect.midleft = self.screen_rect.midleft

        self.y = self.ship_rect.y
        self.x = self.ship_rect.x
        self.move_top = False
        self.move_bottom = False
        self.move_left = False
        self.move_right = False

    def update(self):
        if self.move_top and self.y > 0:
            self.y -= self.settings.ship_speed
        if self.move_bottom and self.ship_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.move_left and self.x > 0:
            self.x -= self.settings.ship_speed
        if self.move_right and self.ship_rect.right < self.screen_rect.right / 2:
            self.x += self.settings.ship_speed

        self.ship_rect.y = self.y
        self.ship_rect.x = self.x

        self.draw()

    def draw(self):
        self.screen.blit(self.ship, self.ship_rect)