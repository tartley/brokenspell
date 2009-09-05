from glob import glob
from os import path
from pyglet.media import load

sounds_dir = path.join('data', 'sounds')

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

