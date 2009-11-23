
from os import environ, pathsep
from platform import system
from sys import argv

from pyglet import options

from gamelib.config import settings


def get_env_name():
    if system() == 'Windows':
        return 'PATH'
    else:
        return 'LD_LIBRARY_PATH'


def append(name, suffix):
    value = environ.get(name, '')
    if value:
        value += pathsep
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


def turn_gl_debug_off():
    options['gl_debug'] = False


def launch():
    from gamelib.application import Application
    application = Application()
    application.launch()


def startup():
    # these functions must be exectued before importing Application
    setup_environment_variables()
    setup_audio()
    turn_gl_debug_off()

    if '-p' in argv or '--profile' in argv:
        import cProfile
        command = 'launch()'
        cProfile.runctx(command, globals(), locals(), filename='profile.out')
    else:
        launch()

