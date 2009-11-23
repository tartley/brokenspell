
from glob import glob

from pyglet import resource
from pyglet.sprite import Sprite

from behaviour import Action
from sounds import play
from worlditem import WorldItem, LEFT, RIGHT


GLIDE_STEER = 0.1
FLAP_STEER = 4
FLAP_LIFT = 6


class Bird(WorldItem):

    def __init__(self, x, y, dx=0, dy=0):
        WorldItem.__init__(self, x, y, dx, dy)
        if self.dx < 0:
            self.facing = LEFT
        else:
            self.facing = RIGHT
        self.can_flap = True
        self.last_flap = None
        self.is_alive = True
        self.actions = set()
        self.foe = None
        self.feathers = 1


    def act(self):
        if Action.FLAP in self.actions:
            if self.can_flap:
                self.dy += FLAP_LIFT
                self.last_flap = 0
                self.can_flap = False
                if self.is_player:
                    play('flap')
        else:
            self.can_flap = True

        ddx = GLIDE_STEER
        if self.last_flap == 0:
            ddx = FLAP_STEER

        if Action.LEFT in self.actions:
            self.dx -= ddx
            self.facing = LEFT
        if Action.RIGHT in self.actions:
            self.dx += ddx
            self.facing = RIGHT


    def choose_frame(self):
        self.frame_idx = 0
        if self.facing == RIGHT:
            self.frame_idx += 1
        if self.is_alive:
            if Action.FLAP in self.actions:
                self.frame_idx += 2
        else:
            self.frame_idx += 4


    def update(self):
        WorldItem.update(self)
        self.actions = self.think()
        self.act()
        self.choose_frame()
        if self.last_flap is not None:
            self.last_flap += 1
        self.rotation = -self.dx * self.dy / 100.0


    def die(self):
        self.is_alive = False
        self.can_fall_off = True


    def collided_with(self, other):
        # TODO: both type check and 'is_alive' test can be moved to collision
        # detection code, to cull collisions before doing the geometry checks
        if isinstance(other, Bird) and other.is_alive and self.is_alive:
            WorldItem.bounce(self, other)
            if (
                self.y < other.y and
                (self.is_player or other.is_player)
            ):
                self.hit(other)
                other.consecutive_feathers = 0
                self.consecutive_feathers = 0
            else:
                if self.is_enemy:
                    self.think.state.face_away(other)

