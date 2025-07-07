from enum import Enum

from components.base import BaseComponent


class AudioSourceProp(Enum):
    IS_PLAYING = 'isPlaying'
    MUTE = 'mute'
    TIME = 'time'
    VOLUME = 'volume'
    CLIP = 'clip'
    TRACK = 'clip.channels'


class AudioSourceMethods(Enum):
    PLAY = 'Play'


class AudioSource(BaseComponent):
    component_assembly = 'UnityEngine.AudioModule'
    component_name = 'UnityEngine.AudioSource'
