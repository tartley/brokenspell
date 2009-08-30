
from pyglet import resource
from pyglet.sprite import Sprite

from behaviour import Think, Hover
from gameent import GameEnt, LEFT, RIGHT


class Enemy(GameEnt):

    SPRITE_PREFIX = 'data/images/Enemy-'

    def __init__(self, *args, **kwargs):
        GameEnt.__init__(self, *args, **kwargs)
        self.behaviour = Hover(self)
        self.last_flap = 0
        self.get_sprite()

    def update(self):
        self.behaviour.update()
        GameEnt.update(self)

