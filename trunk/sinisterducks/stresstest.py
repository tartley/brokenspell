
from random import randint

from pyglet.window import key

from enemy import Enemy
from gameitem import GameItem
from hudpoints import HudPoints


class StressTest(GameItem):

    def __init__(self):
        GameItem.__init__(self)


    def update(self, _):
        if self.game.keystate[key.F1]:
            self.game.add(HudPoints(
                randint(0, self.game.width),
                randint(0, self.game.height),
                randint(0, 8)))


    def on_key_press(self, symbol, modifier):
        if symbol == key.F2:
            for _ in xrange(16):
                Enemy.spawn()
        elif symbol == key.F3:
            for bird in self.game._items[Enemy]:
                bird.feathers += 1
                bird.lose_feather(bird.x, bird.y)

