
from math import atan2, cos, pi, sin
from random import uniform

from pyglet import resource
from pyglet.sprite import Sprite

from gameitem import WorldItem


class Feather(WorldItem):

    is_feather = True
    can_fall_off = True

    def __init__(self, x, y, dx, dy, owner):
        self.owner = owner
        WorldItem.__init__(self, x, y, dx, dy)
        self.AIR_RESIST_Y = uniform(0.7, 0.9)
        self.AIR_RESIST_X = 0.9
        self.rotation = atan2(self.dy, self.dx)
        self.speed = uniform(1, 2)
        self.update_sprite_stats()


    def update(self):
        self.ddx = self.speed * -cos(self.rotation)
        self.ddy = self.speed * sin(self.rotation)
        self.rotation += self.speed / 10
        self.speed *= 0.97
        self.speed -= self.rotation / 100
        WorldItem.update(self)


