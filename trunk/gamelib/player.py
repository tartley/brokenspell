
import math

from pyglet.window import key

from bird import Action, Bird
from feather import Feather


action_map = {
    key.Z:  Action.FLAP,
    key.LEFT: Action.LEFT,
    key.RIGHT: Action.RIGHT,
}


class Player(Bird):

    SPRITE_PREFIX = 'data/sprites/Player-'
    is_player = True

    def __init__(self, keyhandler, x, y):
        Bird.__init__(self, x, y)
        self.keyhandler = keyhandler
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

        if isinstance(other, Bird):
            self.consecutive_feathers = 0

        if isinstance(other, Feather) and other.owner is not self:
            self.consecutive_feathers += 1
            self.level.score += self.consecutive_feathers

