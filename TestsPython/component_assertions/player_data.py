from components.static_components.player_data import PlayerDataProp


def check_tutorial_status(component, is_done):
    assert component.get_static_property(f"{PlayerDataProp.INSTANCE.value}."
                                  f"{PlayerDataProp.TUTORIAL_DONE.value}") == is_done