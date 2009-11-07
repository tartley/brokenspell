
import math

from pyglet.window import key

from bird import Action, Bird
from feather import Feather
from sounds import play


action_map = {
    key.Z:  Action.FLAP,
    key.LEFT: Action.LEFT,
    key.RIGHT: Action.RIGHT,
}


class Player(Bird):

    is_player = True
    image_row = 3

    def __init__(self, keyhandler, x, y, game):
        Bird.__init__(self, x, y)
        self.keyhandler = keyhandler
        self.game = game
        self.consecutive_feathers = 0


    def think(self):
        if not self.is_alive:
            return set()

        actions = set()
        for keypress, action in action_map.iteritems():
            if self.keyhandler[keypress]:
                actions.add(action)
        return actions


    def collided_with(self, other):
        Bird.collided_with(self, other)

        if isinstance(other, Feather):
            if other.owner is not self:
                self.consecutive_feathers += 1
                self.game.score += self.consecutive_feathers
                play('ding', self.consecutive_feathers - 1)
        else:
            self.consecutive_feathers = 0


