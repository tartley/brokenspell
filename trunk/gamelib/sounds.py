
from glob import glob
from os.path import join
from platform import system
from random import randint

from config import settings


sounds_dir = join('data', 'sounds')
sounds = {}

load = None


def init():
    if settings.get('all', 'force_audio') != 'silent':

        try:
            global load
            from pyglet import media
            load = media.load
        except Exception:
            print "WARNING: can't start audio"
            settings.set('all', 'force_audio', 'silent')

        sounds['quack'] = _load_sounds_matching('quack?.ogg')
        sounds['ding'] = _load_sounds_matching('ding?.ogg')
        sounds['die'] = _load_sounds_matching('die?.ogg')
        sounds['ohno'] = [_load_sound('ohno.ogg')]
        sounds['flap'] = [_load_sound('flap.ogg')]


def _load_sound(name):
    return load(join(sounds_dir, name), streaming=False)


def _load_sounds_matching(pattern):
    names = glob(join(sounds_dir, pattern))
    names.sort()
    return [load(n, streaming=False) for n in names]


def play(name, index=None):
    if len(sounds) == 0:
        init()
    if settings.get('all', 'force_audio') == 'silent':
        return
    if index is None:
        index = randint(0, len(sounds[name]) - 1)
    else:
        index = min(index, len(sounds[name]) - 1)
    sounds[name][index].play()
