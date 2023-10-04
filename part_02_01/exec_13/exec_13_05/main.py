import sys
import time
from random import randint

import pygame
from pygame.sprite import Sprite
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class Main:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("横向射击")

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_aliens()

    def run(self):
        while True:
            self.screen.fill(self.settings.background_color)
            self._check_events()

            self._add_bullet()

            if self.stats.game_status:
                self.ship.update()
                self._update_alien()
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

    def _create_aliens(self):
        for number in range(randint(11, 999)):
            self._create_alien()

        print(f"外星人数量：{len(self.aliens)}")

    def _create_alien(self):
        screen_rect = self.screen.get_rect()
        alien = Alien(self)
        alien.x = randint(
            screen_rect.width // 2,
            screen_rect.width - alien.rect.width
        )
        alien.y = randint(0, screen_rect.height - alien.rect.height)
        self.aliens.add(alien)

    def _update_alien(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_alien_leave()

        self.aliens.update()

    def _check_alien_leave(self):
        for alien in self.aliens.sprites():
            if alien.x <= 0:
                print(len(self.aliens), alien.rect.left)
                print('alien hit')
                self._ship_hit()
                break

    def _ship_hit(self):
        print(f"剩余飞船{self.stats.ship_left}")
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_aliens()

            time.sleep(0.5)
        else:
            self.stats.game_status = False

    def _add_bullet(self):
        if len(self.bullets) < self.settings.bullets_allow:
            self.bullets.add(Bullet(self))

    def _update_bullet(self):
        self.bullets.update()

        for bullet in self.bullets.sprites() :
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)

        self._check_bullet_collisions()

    def _check_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        for collision in collisions:
            self.stats.kill_alien += len(collisions[collision])
            print(f"击杀数：{self.stats.kill_alien}")

        if not self.aliens:
            self.bullets.empty()
            self._create_aliens()

    def _update_screen(self):
        self.ship.draw()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    game = Main()
    game.run()