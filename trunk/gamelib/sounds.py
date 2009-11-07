
from glob import glob
from os.path import join
from platform import system
from random import randint

from pyglet.media import load

from config import settings


sounds_dir = join('data', 'sounds')

sounds = {}


def load_sound(name):
    return load(join(sounds_dir, name), streaming=False)


def load_sounds_matching(pattern):
    names = glob(join(sounds_dir, pattern))
    names.sort()
    return [load(n, streaming=False) for n in names]


def play(name, index=None):
    if settings.get('all', 'force_audio') == 'silent':
        return
    if index is None:
        index = randint(0, len(sounds[name]))
    index = min(index, len(sounds[name]) - 1)
    sounds[name][index].play()


if settings.get('all', 'force_audio') != 'silent':
    sounds['quack'] = load_sounds_matching('quack?.ogg')
    sounds['ding'] = load_sounds_matching('ding?.ogg')
    sounds['die'] = load_sounds_matching('die?.ogg')
    sounds['ohno'] = [load_sound('ohno.ogg')]
    sounds['flap'] = [load_sound('flap.ogg')]

