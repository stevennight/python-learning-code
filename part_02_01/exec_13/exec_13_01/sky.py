import sys
from random import randint

import pygame
from star import Star

class Sky:
    """星空"""

    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("sky")

        self.stars = pygame.sprite.Group()

        self._add_star()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((0, 0, 255))
            self.stars.draw(self.screen)
            pygame.display.flip()

    def _add_star(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_rect.width
        available_space_y = self.screen_rect.height
        number_cols = available_space_x // (2 * star_width)
        number_rows = available_space_y // (2 * star_height)

        for col in range(number_cols):
            for row in range(number_rows):
                display_random = randint(0, 3)
                if display_random > 2 :
                    continue
                rotate_degree = randint(0, 360)
                star = Star(self, rotate_degree)
                offset_x = randint(-star_width, star_width)
                offset_y = randint(-star_height, star_height)
                star.x += col * 2 * star_width + offset_x
                star.y += row * 2 * star_height + offset_y

                star.rect.x = star.x
                star.rect.y = star.y
                self.stars.add(star)



if __name__ == '__main__':
    sky = Sky()
    sky.run()