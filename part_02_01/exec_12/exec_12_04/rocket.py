import pygame


class Rocket:
    """这是一个火箭"""

    def __init__(self, main):
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()

        self.rocket = pygame.image.load('images/ship.bmp')
        self.rocket_rect = self.rocket.get_rect()
        self.rocket_rect.center = self.screen_rect.center

        self.move_left = False
        self.move_right = False
        self.move_top = False
        self.move_bottom = False

    def update(self):
        if self.move_left:
            self.rocket_rect.x -= 10
        if self.move_right:
            self.rocket_rect.x += 10
        if self.move_top:
            self.rocket_rect.y -= 10
        if self.move_bottom:
            self.rocket_rect.y += 10

        print(self.rocket_rect.x)
        print(self.rocket_rect.y)

        if self.rocket_rect.x < 0:
            self.rocket_rect.x = 0
        elif self.rocket_rect.x > self.screen_rect.width - self.rocket_rect.width:
            self.rocket_rect.x = self.screen_rect.width - self.rocket_rect.width

        if self.rocket_rect.y < 0:
            self.rocket_rect.y = 0
        elif self.rocket_rect.y > self.screen_rect.height - self.rocket_rect.height:
            self.rocket_rect.y = self.screen_rect.height - self.rocket_rect.height


    def draw(self):
        self.screen.blit(self.rocket, self.rocket_rect)