
import math

from pyglet.window import key

from bird import Action, Bird
from feather import Feather


class Player(Bird):

    SPRITE_PREFIX = 'data/images/Player-'
    is_player = True

    def __init__(self, keyhandler, x, y):
        Bird.__init__(self, x, y)
        self.keyhandler = keyhandler


    def reset(self, *args):
        Bird.reset(self, *args)
        self.think = lambda: Player.think(self)
        self.can_fall_off = False


    def think(self):
        action_map = {
            key.Z:  Action.FLAP,
            key.LEFT: Action.LEFT,
            key.RIGHT: Action.RIGHT,
        }
        actions = set()
        if self.is_alive:
            for keypress, action in action_map.iteritems():
                if self.keyhandler[keypress]:
                    actions.add(action)
        return actions


    def collided_with(self, other):
        Bird.collided_with(self, other)
        if isinstance(other, Feather):
            self.level.score += 10

