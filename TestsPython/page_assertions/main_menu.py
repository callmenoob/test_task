def is_displayed(page):
    assert (page.store_button
            and page.leader_board_button
            and page.settings_button
            and page.mission_button
            and page.run_button
            and page.character_name
            and page.theme_name)


def check_tutorial_overlay(page, should_be_present=True):
    assert page.tutorial_overlay.enabled == should_be_present
