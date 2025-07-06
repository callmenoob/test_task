import operator as op

from alttester import AltObject

from components.audio_source import AudioSource, AudioSourceProp


def is_audio_playing(component: AltObject):
    assert AudioSource.get_component_property(component, AudioSourceProp.IS_PLAYING)


def check_audio_clip_name(component: AltObject, expected_clip_name: str):
    assert AudioSource.get_component_property(component, AudioSourceProp.CLIP)['name'] == expected_clip_name


def check_audio_track_execution_time(component: AltObject, expected_playback_time: float, operator: callable =op.gt):
    assert operator(AudioSource.get_component_property(component, AudioSourceProp.time), expected_playback_time)
