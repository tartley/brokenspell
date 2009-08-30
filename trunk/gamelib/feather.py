
from pyglet import resource
from pyglet.sprite import Sprite

from gameent import GameEnt

class Feather(GameEnt):
    
    GRAVITY = 0.1

    def __init__(self, *args, **kwargs):
        GameEnt.__init__(self, *args, **kwargs)
        self.sprite = Sprite(resource.image('data/images/feather.png'))
        self.update_sprite_stats(self.sprite)
        self.canDie = False


    def get_sprite(self):
        return self.sprite
