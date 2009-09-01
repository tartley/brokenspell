
import math
from itertools import count
from random import uniform

from pyglet import resource
from pyglet.sprite import Sprite

from gameent import GameEnt

class Feather(GameEnt):
    
    is_feather = True
    can_fall_off = True

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner')
        GameEnt.__init__(self, *args, **kwargs)
        self.AIR_RESIST_Y = uniform(0.6, 0.9)
        self.AIR_RESIST_X = 0.9
        self.sprite = Sprite(resource.image('data/images/feather.png'))
        self.update_sprite_stats(self.sprite)

        self.sine_gen = sine_curve()
        self.saw_gen = saw_curve()

    def get_sprite(self):
        return self.sprite


    def update(self):
        self.ddx = self.sine_gen.next()
        self.ddy = self.saw_gen.next()
        GameEnt.update(self)


    def collided_with(self, other):
        pass


def sine_curve():
    to_rad = 2 * math.pi / 360.0
    for degrees in count():
        yield math.sin(degrees * 2 * to_rad) / 10

def saw_curve():
    for t in count():
        yield ((t % 7) - 3) / 4.0
