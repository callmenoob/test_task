from components.audio_source import AudioSource, AudioSourceMethods
from components.game_state import GameStateMethods, GameState
from pages.base_page import BasePage
from alttester import By, AltDriver


class StartPage(BasePage):
    def __init__(self, altdriver: AltDriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Start')

    @property
    def start_button(self):
        return self.altdriver.find_object(By.NAME, 'StartButton')

    @property
    def start_text(self):
        return self.altdriver.find_object(By.NAME, 'StartText')

    @property
    def logo_image(self):
        return self.altdriver.find_object(By.NAME, 'LogoImage')

    @property
    def unity_url_button(self):
        return self.altdriver.find_object(By.NAME, 'UnityURLButton')

    def press_start(self):
        self.start_button.tap()

    def emulate_press_start(self):
        AudioSource.call_component_method(self.start_button, AudioSourceMethods.PLAY)

    def get_start_button_text(self):
        return self.start_text.get_text()
