import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class Main:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("横向射击")

        self.ship = Ship(self)
        self.bullets = []

    def run(self):
        while True:
            self._check_events()
            self._update_bullet()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_event_key_down(event)
            if event.type == pygame.KEYUP:
                self._check_event_key_up(event)

    def _check_event_key_down(self, event):
        if event.key == pygame.K_UP:
            self.ship.move_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_bottom = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_SPACE:
            self._add_bullet()

    def _check_event_key_up(self, event):
        if event.key == pygame.K_UP:
            self.ship.move_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_bottom = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = False

    def _add_bullet(self):
        if len(self.bullets) < self.settings.bullets_allow:
            self.bullets.append(Bullet(self))

    def _update_bullet(self):
        for bullet in self.bullets:
            bullet.update()

        for bullet in self.bullets[:]:
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.ship.update()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    game = Main()
    game.run()