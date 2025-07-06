from enum import Enum

from alttester import AltDriver

from components.static_components.base import StaticBaseComponent
from constants import CS_ASSEMBLY


class PlayerDataEditorMethods(Enum):
    CLEAR_SAVE = 'ClearSave'


class PlayerDataEditor(StaticBaseComponent):
    component_name = 'PlayerDataEditor'
    component_assembly = CS_ASSEMBLY

    def __init__(self, altdriver: AltDriver):
        super().__init__(altdriver)
