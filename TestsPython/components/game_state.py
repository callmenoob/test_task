from enum import Enum

from components.base import BaseComponent
from constants import CS_ASSEMBLY

class GameStateMethods(Enum):
    FINISH_TUTORIAL = 'FinishTutorial'


class GameState(BaseComponent):
    component_name = 'GameState'
    component_assembly = CS_ASSEMBLY