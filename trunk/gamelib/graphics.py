
from glob import glob
from os.path import join

from pyglet import image


SPRITES_DIR = join('data', 'sprites')


def load_sprite_images():
    images = {}
    files = glob('%s/*.png' % (SPRITES_DIR))
    for filename in files:
        filename = filename.replace('\\', '/')
        name = filename[len(SPRITES_DIR) + 1:-4]
        images[name] = image.load(filename)
    return images

