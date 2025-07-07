from enum import Enum

from alttester import AltDriver

from components.static_components.base import StaticBaseComponent
from constants import CS_ASSEMBLY


class PlayerDataProp(Enum):
    INSTANCE = 'instance'
    TUTORIAL_DONE = 'tutorialDone'
    COINS = 'coins'


class PlayerDataMethods(Enum):
    CREATE_PLAYER = 'Create'
    NEW_SAVE = 'NewSave'


class PlayerData(StaticBaseComponent):
    component_name = 'PlayerData'
    component_assembly = CS_ASSEMBLY

    def __init__(self, altdriver: AltDriver):
        super().__init__(altdriver)
