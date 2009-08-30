
from gameent import GameEnt, LEFT, RIGHT


GLIDE_STEER = 0.3
FLAP_STEER = 6
FLAP_LIFT = 13


class Action(object):
    FLAP = 0
    LEFT = 1
    RIGHT = 2


class Bird(GameEnt):

    def __init__(self, *args, **kwargs):
        GameEnt.__init__(self, *args, **kwargs)
        self.can_flap = True
        self.last_flap = None


    def act(self, actions):
        if Action.FLAP in actions:
            if self.can_flap:
                self.flap()
        else:
            self.can_flap = True

        ddx = GLIDE_STEER
        if self.last_flap == 0:
            ddx = FLAP_STEER

        if Action.LEFT in actions:
            self.dx -= ddx
            self.facing = LEFT
        if Action.RIGHT in actions:
            self.dx += ddx
            self.facing = RIGHT


    def flap(self):
        self.dy += FLAP_LIFT
        self.last_flap = 0
        self.can_flap = False


    def update(self):
        GameEnt.update(self)
        actions = self.think()
        self.act(actions)
        if self.last_flap is not None:
            self.last_flap += 1 

