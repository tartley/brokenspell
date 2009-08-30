
from pyglet.window import key

from gameent import GameEnt, LEFT, RIGHT


GLIDE_STEER = 0.3
FLAP_STEER = 6
FLAP_LIFT = 13


class Player(GameEnt):

    SPRITE_PREFIX = 'data/images/Player-'

    def __init__(self, keyhandler, *args):
        GameEnt.__init__(self, *args)
        self.keyhandler = keyhandler
        self.can_flap = True
        self.last_flap = None


    def read_controls(self):
        if self.last_flap is not None:
            self.last_flap += 1

        if self.keyhandler[key.Z]:
            if self.can_flap:
                self.flap()
        else:
            self.can_flap = True

        ddx = GLIDE_STEER
        if self.last_flap == 0:
            ddx = FLAP_STEER

        if self.keyhandler[key.LEFT]:
            self.dx -= ddx
            self.facing = LEFT
        if self.keyhandler[key.RIGHT]:
            self.dx += ddx
            self.facing = RIGHT


    def flap(self):
        if self.can_flap:
            self.dy += FLAP_LIFT
            self.last_flap = 0
            self.can_flap = False


    def update(self):
        self.read_controls()
        GameEnt.update(self)

