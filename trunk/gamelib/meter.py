
from pyglet import image

class Meter(object):

    IMG_METER = 'data/images/meter.png'
    HIGH_VALUE = 20


    def __init__(self, level_height):
        self.level_height = level_height
        self.image = image.load(self.IMG_METER)
        self.max_height = self.image.height
        self.value = 0


    def draw(self):
        sub_height = self.calc_height()
        if sub_height == 0:
            return
        sub_image = self.image.get_region(0, 0, self.image.width, sub_height)
        sub_image.blit(7, self.level_height - self.max_height - 7)


    def calc_height(self):
        height = self.max_height * self.value / self.HIGH_VALUE
        return min(self.max_height, height)
