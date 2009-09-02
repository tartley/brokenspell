from glob import glob
from os import path
from pyglet.media import load

quack_names = glob(path.join('data', 'sounds', 'quack?.ogg'))
quacks = [load(f, streaming=False) for f in quack_names]
