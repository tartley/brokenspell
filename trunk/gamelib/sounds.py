from glob import glob
from os import path
from pyglet.media import load

sounds_dir = path.join('data', 'sounds')
quack_names = glob(path.join(sounds_dir, 'quack?.ogg'))
quacks = [load(f, streaming=False) for f in quack_names]

ohno = load(path.join(sounds_dir, 'ohno.ogg'), streaming=False)
