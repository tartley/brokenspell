
from pyglet import resource
from pyglet.sprite import Sprite

from behaviour import Thinker
from bird import Bird


class Enemy(Bird):

    SPRITE_PREFIX = 'data/images/Enemy-'
    is_enemy = True

    def __init__(self, x, y, dx=0, dy=0, feathers=2):
        Bird.__init__(self, x, y, dx, dy, feathers)
        self.think = Thinker(self)
        self.last_flap = 0

