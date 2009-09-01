
from math import atan2, cos, pi, sin, degrees
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

        self.rotation = atan2(self.dy, self.dx)
        self.speed = 1


    def get_sprite(self):
        self.sprite.rotation = degrees(self.rotation)
        return self.sprite


    def update(self):
        self.ddx = self.speed * -cos(self.rotation)
        self.ddy = self.speed * sin(self.rotation)
        self.rotation = sin(self.level.age * 2)
        self.speed *= 0.99
        self.speed -= self.rotation / 100
        GameEnt.update(self)


    def collided_with(self, other):
        pass

