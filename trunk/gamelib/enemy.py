
from pyglet import resource
from pyglet.sprite import Sprite

from gameent import GameEnt, LEFT, RIGHT


class Enemy(GameEnt):

    def __init__(self, *args, **kwargs):
        GameEnt.__init__(self, *args, **kwargs)
        self.sprites[LEFT] = \
            Sprite(resource.image('data/images/Enemy-flight-L.png'))
        self.sprites[RIGHT] = \
            Sprite(resource.image('data/images/Enemy-flight-R.png'))


