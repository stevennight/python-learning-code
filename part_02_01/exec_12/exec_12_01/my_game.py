import sys

import pygame.display


class MyGame:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('练习12-01')

        self.plane = Plane(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((0, 0, 255))

            self.plane.blitem()

            pygame.display.flip()


class Plane:

    def __init__(self, my_game):
        self.screen = my_game.screen
        self.screen_rect = my_game.screen.get_rect()
        self.plane = pygame.image.load('images/ship.bmp').convert_alpha()
        self.plane_rect = self.plane.get_rect()

        self.plane_rect.midbottom = self.screen_rect.midbottom

    def blitem(self):
        self.screen.blit(self.plane, self.plane_rect)


if __name__ == '__main__':
    my_game = MyGame()
    my_game.run_game()