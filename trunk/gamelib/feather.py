
from math import atan2, copysign, cos, pi, sin, sqrt
from random import uniform

from pyglet import clock, resource
from pyglet.sprite import Sprite

from worlditem import GRAVITY, WorldItem


AIR_RESIST = 0.99
GRAVITY = 1


class Feather(WorldItem):

    is_feather = True
    can_fall_off = True

    def __init__(self, x, y, dx, _, owner):
        WorldItem.__init__(self, x, y, 0, 0)
        self.rotation = 0
        self.speed = copysign(uniform(5, 52), -dx)
        self.curve = uniform(0.002, 0.02)
        self.owner = owner
        clock.schedule_once(lambda _: self.reset_owner(), 1)


    def reset_owner(self):
        self.owner = None


    def update(self, dt):
        self.rotation += (self.speed * self.curve) * dt
        self.speed *= (1 - (max(0, (abs(self.speed) - 7)) * self.curve)) ** dt
        self.speed -= sin(self.rotation) / 2 * dt

        self.x += self.speed * -cos(self.rotation) * dt
        self.y += (self.speed * sin(self.rotation) - GRAVITY) * dt

        WorldItem.test_for_fall_off_screen(self)

