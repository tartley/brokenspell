from glob import glob
from os import path
from pyglet.media import load

sounds_dir = path.join('data', 'sounds')

def load_sounds_matching(pattern):
    names = glob(path.join(sounds_dir, pattern))
    names.sort()
    return [load(n, streaming=False) for n in names]

quacks = load_sounds_matching('quack?.ogg')
ohno = load_sounds_matching('ohno.ogg')[0]
dings = load_sounds_matching('ding?.ogg')
