
from pyglet import resource
from pyglet.sprite import Sprite
from pyglet.window import key

from gameent import GameEnt, LEFT, RIGHT


GLIDE_STEER = 0.3
FLAP_STEER = 6
FLAP_LIFT = 13


class Player(GameEnt):

    def __init__(self, *args):
        GameEnt.__init__(self, *args)
        self.can_flap = True
        self.sprites[LEFT] = \
            Sprite(resource.image('data/images/Player-flap-L.png'))
        self.sprites[RIGHT] = \
            Sprite(resource.image('data/images/Player-flap-R.png'))


    def read_controls(self, keyhandler):
        if keyhandler[key.Z]:
            flapping = self.try_flap()
        else:
            self.can_flap = True
            flapping = False

        ddx = GLIDE_STEER
        if flapping:
            ddx = FLAP_STEER

        if keyhandler[key.LEFT]:
            self.dx -= ddx
            self.facing = LEFT
        if keyhandler[key.RIGHT]:
            self.dx += ddx
            self.facing = RIGHT


    def try_flap(self):
        if self.can_flap:
            self.dy += FLAP_LIFT
            self.can_flap = False
            return True
        return False

