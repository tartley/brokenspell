
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


    def get_sprite(self):
        return self.sprite


    def update(self):
        GameEnt.update(self)


    def collided_with(self, other):
        pass

