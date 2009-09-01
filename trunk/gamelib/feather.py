
from random import uniform
from math import pi, sin

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

        self.drift_phase = uniform(0, 2*pi)
        self.drift_frequency = uniform(0, 2)
        self.drift_amplitude = 0.5 # uniform(0, 1)


    def get_sprite(self):
        return self.sprite


    def update(self):
        GameEnt.update(self)
        self.ddx +=  self.drift_amplitude * sin(
            self.level.age * self.drift_frequency + self.drift_phase)


    def collided_with(self, other):
        pass

