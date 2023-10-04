import sys

import pygame
from settings import Settings
from water import Water


class Rain:
    """下雨"""

    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Rain")

        self.water_group = pygame.sprite.Group()
        self._create_line_water()

    def run(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_line_water(self):
        water = Water(self)
        water.width, water.height = water.rect.size
        water_area_width = self.settings.rain_inter + water.rect.width
        screen_rect = self.screen.get_rect()
        number_cols = screen_rect.width // water_area_width

        for col_number in range(number_cols):
            self._create_water(col_number)

    def _create_water(self, col_index):
        water = Water(self)
        water_area_width = self.settings.rain_inter + water.rect.width
        # 雨滴画中间，左右两边间隔相等，所以画的时候画在间隔整除2的位置。
        water_position_offset = self.settings.rain_inter // 2
        water.x = col_index * (water_area_width) + (water_position_offset)
        water.rect.x = water.x

        self.water_group.add(water)

    def _remove_water(self):
        clear = False
        for water in self.water_group.sprites():
            if water.rect.top >= self.screen.get_rect().bottom:
                clear = True

        if clear:
            self.water_group = pygame.sprite.Group()
            self._create_line_water()

    def _update_water(self):
        self._remove_water()
        self.water_group.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self._update_water()
        pygame.display.flip()


if __name__ == '__main__':
    rain = Rain()
    rain.run()
