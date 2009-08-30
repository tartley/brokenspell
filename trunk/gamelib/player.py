
import math

from pyglet.window import key

from bird import Action, Bird


class Player(Bird):

    SPRITE_PREFIX = 'data/images/Player-'

    def __init__(self, keyhandler, x, y):
        Bird.__init__(self, x, y)
        self.keyhandler = keyhandler
        self.is_player = True


    def think(self):
        action_map = {
            key.Z:  Action.FLAP,
            key.LEFT: Action.LEFT,
            key.RIGHT: Action.RIGHT,
        }
        actions = set()
        for keypress, action in action_map.iteritems():
            if self.keyhandler[keypress]:
                actions.add(action)
        return actions

