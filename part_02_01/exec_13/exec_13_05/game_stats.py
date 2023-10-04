class GameStats:
    def __init__(self, main):
        self.setting = main.settings

        self.game_status = True
        self.ship_left = 0
        self.kill_alien = 0

        self.reset_stats()

    def reset_stats(self):
        self.game_status = True
        self.ship_left = self.setting.ship_num
        self.kill_alien = 0
