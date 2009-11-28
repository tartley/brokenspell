
from pyglet.window import key

from gameitem import GameItem


class GameControls(GameItem):

    def __init__(self):
        GameItem.__init__(self)
        self.hudpoints_shower = False


    def on_key_press(self, symbol, _):
        if symbol == key.F1:
            self.hudpoints_shower = not self.hudpoints_shower
        elif symbol == key.F2:
            for _ in xrange(16):
                Enemy.spawn(self.game)
        elif symbol == key.F3:
            for bird in self.items[Enemy]:
                bird.feathers += 1
                bird.lose_feather(bird.x, bird.y)


    def update(self):
        if self.hudpoints_shower:
            self.game.add(HudPoints(
                randint(0, self.game.width),
                randint(0, self.game.height),
                randint(0, 8)))

