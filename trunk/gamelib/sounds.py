from glob import glob
from os import path
from platform import system

from pyglet import options
from pyglet.media import load

from gamelib.config import settings

sounds_dir = path.join('data', 'sounds')


def setup():
    force_audio = settings.get('all', 'force_audio')
    if force_audio:
        options['audio'] = (force_audio,)
    else:
        if system() == 'Windows':
            options['audio'] = ('directsound', 'openal', 'silent')
        else:
            options['audio'] = ('alsa', 'openal', 'silent')


def load_sound(name):
    return load(path.join(sounds_dir, name), streaming=False)


def load_sounds_matching(pattern):
    names = glob(path.join(sounds_dir, pattern))
    names.sort()
    return [load(n, streaming=False) for n in names]


quacks = load_sounds_matching('quack?.ogg')
dings = load_sounds_matching('ding?.ogg')
dies = load_sounds_matching('die?.ogg')
ohno = load_sound('ohno.ogg')
flap = load_sound('flap.ogg')

