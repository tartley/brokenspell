
from ctypes import cdll
from os import environ, pathsep
from os.path import join
from platform import system
from subprocess import call
import sys

from pyglet import options

from .config import settings
from . import VERSION


def process_args():
    if '--version' in sys.argv:
        print VERSION
        sys.exit()


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
            options['audio'] = ('openal', 'alsa', 'silent')


def turn_gl_debug_off():
    '''
    Turn off error checking on opengl calls. This can make a huge improvement
    to performance.
    '''
    options['gl_debug'] = False


def launch():
    from .application import Application
    application = Application()
    application.launch()


def startup():
    # these functions must be executed before importing Application
    process_args()
    setup_environment_variables()
    setup_audio()
    turn_gl_debug_off()
    launch()

