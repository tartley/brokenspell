import random

from behaviour import Thinker, Plummet
from bird import Bird
from feather import Feather
from sounds import play


class Enemy(Bird):

    is_enemy = True

    def __init__(self, x, y, dx=0, dy=0):
        Bird.__init__(self, x, y, dx, dy)
        self.think = Thinker(self)
        self.last_flap = 0


    def hit(self, other):
        Bird.die(self)
        self.think.state = Plummet(self)
        self.lose_feather(other.x, other.y)


    def lose_feather(self, otherx, othery):
        play('quack')
        self.feathers -= 1
        dx = self.x - otherx
        dy = self.y - othery
        feather = Feather(
            self.x, self.y,
            dx, dy,
            self)
        self.arena.add(feather)

