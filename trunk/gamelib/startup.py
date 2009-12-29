
from os import environ, pathsep
from os.path import join
from platform import system
from sys import stderr
from subprocess import call

from pyglet import options

from gamelib.config import settings


def install_ms_visual_c_runtime():
    '''
    Installs DLLs which are required when running under py2exe on Windows
    '''
    if system() == 'Windows':
        # TODO, only do this if required DLL is not already installed
        command = [join('lib', 'vcredist_x86.exe'), '/q']
        retcode = call(command)
        if retcode != 0:
            stderr.write(
                'Return value %d from vcredist_x86.exe\n' % (retcode,))


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
    '''
    Turn off error checking on opengl calls. This can make a huge improvement
    to performance.
    '''
    options['gl_debug'] = False


def launch():
    from gamelib.application import Application
    application = Application()
    application.launch()


def startup():
    # these functions must be executed before importing Application
    install_ms_visual_c_runtime()
    setup_environment_variables()
    setup_audio()
    turn_gl_debug_off()
    launch()

