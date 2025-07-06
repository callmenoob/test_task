from pages.base_page import BasePage
from alttester import By, AltDriver


class MainMenuPage(BasePage):

    def __init__(self, altdriver: AltDriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Main')

    @property
    def character(self):
        return self.altdriver.wait_for_object(By.NAME, 'PlayerPivot', timeout=2)

    @property
    def store_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'StoreButton', timeout=2)

    @property
    def leader_board_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'OpenLeaderboard', timeout=2)

    @property
    def settings_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'SettingButton', timeout=2)

    @property
    def mission_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'MissionButton', timeout=2)

    @property
    def run_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'StartButton', timeout=2)

    @property
    def character_name(self):
        return self.altdriver.wait_for_object(By.NAME, 'CharName', timeout=2)

    @property
    def theme_name(self):
        return self.altdriver.wait_for_object(By.NAME, 'ThemeZone', timeout=2)

    @property
    def tutorial_overlay(self):
        return self.altdriver.wait_for_object(By.NAME, 'TutorialOverlay', timeout=2, enabled=False)

    def press_run(self):
        self.run_button.tap()
