
from glob import glob
from os.path import join

from pyglet import image


IMG_GROUND = 'data/images/ground.png'
SPRITE_FILE = 'data/spritesheet.png'
SPRITES_DIR = join('data', 'sprites')


BIRD_SIZE = 64


class Graphics(object):

    def __init__(self):
        self.spritesheet = None
        self.player = []
        self.enemy = []
        self.feather = None


    def load(self):
        self.ground = image.load(IMG_GROUND)
        self.spritesheet = image.load(SPRITE_FILE)

        self.player = self.get_regions(BIRD_SIZE, row=0)
        self.enemy = self.get_regions(BIRD_SIZE, row=1)
        self.feather = self.spritesheet.get_region(
            0, 8 * 64, 16, 8 * 64 + 16)


    def get_regions(self, size, row):
        return [
            self.spritesheet.get_region(
                x * size, row * size, (x + 1) * size, (row + 1) * size)
            for x in xrange(0, self.spritesheet.width / size)
        ]


def load_sprite_images():
    images = {}
    files = glob('%s/*.png' % (SPRITES_DIR))
    for filename in files:
        filename = filename.replace('\\', '/')
        name = filename[len(SPRITES_DIR) + 1:-4]
        images[name] = image.load(filename)
    return images

