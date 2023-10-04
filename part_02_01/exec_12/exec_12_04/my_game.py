import sys

import pygame
from rocket import Rocket


class MyGame:
    """练习12-4"""

    def __init__(self):
        """初始化窗口与元素"""
        self.screen = pygame.display.set_mode(
            (0, 0),
            pygame.FULLSCREEN
        )
        pygame.display.set_caption("火箭游戏")

        self.rocket = Rocket(self)

    def run(self):
        while True:
            """循环执行 事件检测与刷新"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.rocket.move_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.rocket.move_right = False
                    elif event.key == pygame.K_UP:
                        self.rocket.move_top = False
                    elif event.key == pygame.K_DOWN:
                        self.rocket.move_bottom = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.rocket.move_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.rocket.move_right = True
                    elif event.key == pygame.K_UP:
                        self.rocket.move_top = True
                    elif event.key == pygame.K_DOWN:
                        self.rocket.move_bottom = True

                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.rocket.update()

            self.screen.fill((255, 255, 255))
            self.rocket.draw()
            pygame.display.flip()


if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()
