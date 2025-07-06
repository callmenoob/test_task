import os
import sys

from alttester import By, AltDriver

sys.path.append(os.path.dirname(__file__))


class BasePage:

    def __init__(self, altdriver: AltDriver):
        self.altdriver = altdriver

    @property
    def music_player(self):
        return self.altdriver.find_object(By.NAME, 'MusicPlayer')
