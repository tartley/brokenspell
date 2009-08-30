
from pyglet import resource
from pyglet.sprite import Sprite

from behaviour import Thinker
from bird import Bird


class Enemy(Bird):

    SPRITE_PREFIX = 'data/images/Enemy-'

    def __init__(self, *args, **kwargs):
        Bird.__init__(self, *args, **kwargs)
        self.think = Thinker(self)
        self.last_flap = 0

