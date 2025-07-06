from enum import Enum

from components.base import BaseComponent


class AudioSourceProp(Enum):
    IS_PLAYING = 'isPlaying'
    MUTE = 'mute'
    time = 'time'
    volume = 'volume'
    CLIP = 'clip'
    track = 'clip.channels'
    TIME = 'time'


class AudioSourceMethods(Enum):
    PLAY = 'Play'

class AudioSource(BaseComponent):
    component_assembly = 'UnityEngine.AudioModule'
    component_name = 'UnityEngine.AudioSource'


