import pytest
from alttester import AltDriver

from component_assertions import player_data
from components.static_components.player_data import PlayerData
from components.static_components.player_data_editor import PlayerDataEditor
from pages.game_play_page import GamePlayPage
from pages.main_menu_page import MainMenuPage
from page_assertions import main_menu


class TestMainMenuPage():
    @pytest.fixture(autouse=True)
    def setup_method(self, altdriver: AltDriver):
        self.main_menu_page = MainMenuPage(altdriver)
        self.game_play = GamePlayPage(altdriver)
        self.editor = PlayerDataEditor(altdriver)
        self.player_data = PlayerData(altdriver)

    def test_main_menu_page_loaded_correctly(self):
        self.main_menu_page.load()
        main_menu.is_displayed(self.main_menu_page)
        main_menu.check_tutorial_overlay(self.main_menu_page)

    def test_main_manu_completed_tutorial(self):
        self.main_menu_page.load()
        player_data.check_tutorial_status(self.player_data, False)
        self.main_menu_page.press_run()
        self.game_play.skip_tutorial()
        main_menu.check_tutorial_overlay(self.main_menu_page, False)
        player_data.check_tutorial_status(self.player_data, True)
