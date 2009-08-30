
from pyglet import resource
from pyglet.sprite import Sprite

from behaviour import Thinker
from bird import Bird


class Enemy(Bird):

    SPRITE_PREFIX = 'data/images/Enemy-'

    def __init__(self, x, y, dx=0, dy=0, feathers=2):
        Bird.__init__(self, x, y, dx, dy)
        self.think = Thinker(self)
        self.last_flap = 0
        self.feathers = feathers


    def update(self):
        Bird.update(self)
        if self.feathers == 0:
            self.is_gone = True

