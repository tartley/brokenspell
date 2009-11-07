import random

from behaviour import Thinker, Plummet
from bird import Bird
from sounds import play


class Enemy(Bird):

    is_enemy = True

    def __init__(self, x, y, dx=0, dy=0, feathers=2):
        Bird.__init__(self, x, y, dx, dy, feathers)
        self.think = Thinker(self)
        self.last_flap = 0


    def die(self):
        Bird.die(self)
        play('die')
        self.think.state = Plummet(self)


    def lose_feather(self, x, y):
        Bird.lose_feather(self, x, y)
        play('quack')

