
from os import environ
from platform import system

from pyglet import options

from gamelib.config import settings


def get_separator():
    if system() == 'Windows':
        return ';'
    else:
        return ':'


def get_env_name():
    if system() == 'Windows':
        return 'PATH'
    else:
        return 'LD_LIBRARY_PATH'


def append(name, suffix):
    value = environ.get(name, '')
    if value:
        value += get_separator()
    value += suffix
    environ[name] = value


def setup_environment_variables():
    append(get_env_name(), 'lib')


def setup_audio():
    force_audio = settings.get('all', 'force_audio')
    if force_audio:
        options['audio'] = (force_audio,)
    else:
        if system() == 'Windows':
            options['audio'] = ('directsound', 'openal', 'silent')
        else:
            options['audio'] = ('alsa', 'openal', 'silent')


def pre_run():
    setup_environment_variables()
    setup_audio()
