import time
import pytest
from alttester import AltDriver

from component_assertions.audio import is_audio_playing, check_audio_clip_name, \
    check_audio_track_execution_time

from constants import CLICK_BUTTON_PRESS_CLIP

from page_assertions import start_page
from page_assertions import main_menu
from pages.start_page import StartPage
from pages.main_menu_page import MainMenuPage

MAIN_CLIP_NAME = 'MenuTheme'


class TestStartPage():
    @pytest.fixture(autouse=True)
    def setup_method(self, altdriver: AltDriver):
        self.start_page = StartPage(altdriver)
        self.start_page.load()
        self.main_menu_page = MainMenuPage(altdriver)

    def test_start_page_loaded_correctly(self):
        start_page.is_displayed(self.start_page)
        is_audio_playing(self.start_page.music_player)
        check_audio_clip_name(self.start_page.music_player, MAIN_CLIP_NAME)

    def test_start_button_loads_main_menu(self):
        start_time = time.time()
        time.sleep(1)  # to add some time to track playback
        self.start_page.press_start()

        new_page_time = time.time()
        timespan = new_page_time - start_time
        main_menu.is_displayed(self.main_menu_page)
        check_audio_track_execution_time(self.main_menu_page.music_player, timespan)

    def test_ui_start_button_sound(self):
        # since button press loads new scene, emulating button press to check click sound
        self.start_page.emulate_press_start()
        is_audio_playing(self.start_page.start_button)
        check_audio_track_execution_time(self.start_page.start_button, 0.1)
        check_audio_clip_name(self.start_page.start_button, CLICK_BUTTON_PRESS_CLIP)
