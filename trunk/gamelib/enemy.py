from random import uniform

from behaviour import Thinker, Plummet
from bird import Bird
from feather import Feather
from sounds import play


class Enemy(Bird):

    is_enemy = True
    count = 0

    def __init__(self, x, y, dx=0, dy=0):
        Bird.__init__(self, x, y, dx, dy)
        self.think = Thinker(self)
        self.last_flap = 0


    @staticmethod
    def spawn(_):
        x = uniform(0, Enemy.game.width)
        y = Enemy.game.height + 32
        dx = uniform(-20, 20)
        dy = 0
        Enemy.game.add(Enemy(x, y, dx=dx, dy=0))


    def added(self):
        Bird.added(self)
        Enemy.count += 1


    def removed(self):
        Enemy.count -= 1
        if Enemy.count == 0 and not self.is_alive:
            self.game.spawn_wave()


    def hit(self, other):
        Bird.die(self)
        self.think.state = Plummet(self)
        play('quack')
        self.lose_feather(other.x, other.y)


    def lose_feather(self, otherx, othery):
        self.feathers -= 1
        dx = self.x - otherx
        dy = self.y - othery
        self.game.add(Feather(self.x, self.y, dx, dy, self))

