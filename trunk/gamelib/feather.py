
from math import atan2, cos, pi, sin, sqrt
from random import uniform

from pyglet import clock, resource
from pyglet.sprite import Sprite

from worlditem import GRAVITY, WorldItem


AIR_RESIST = 0.995


class Feather(WorldItem):

    is_feather = True
    can_fall_off = True

    def __init__(self, x, y, dx, dy, owner):
        WorldItem.__init__(self, x, y, dx, dy)
        self.rotation = uniform(-0.5, 0.5)
        self.speed = uniform(5, 12)
        self.curve = uniform(0.002, 0.02)
        self.owner = owner
        clock.schedule_once(lambda _: self.reset_owner(), 1)


    def reset_owner(self):
        self.owner = None


    def update(self):
        self.rotation += self.speed * self.curve
        self.speed *= AIR_RESIST
        self.speed -= sin(self.rotation) / 2

        self.x += self.speed * -cos(self.rotation)
        self.y += self.speed * sin(self.rotation) - GRAVITY

        WorldItem.test_for_fall_off_screen(self)

