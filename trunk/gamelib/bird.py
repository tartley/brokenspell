
from glob import glob
from math import atan2, sqrt

from pyglet import resource
from pyglet.sprite import Sprite

from behaviour import Action
from sounds import play
from vec2 import Vec2
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


    def sprite_rotation(self):
        # use different dynamics to rotate bird sprite depending on if
        # bird is rising or falling
        if self.dy < 0:
            speed = sqrt(self.dx * self.dx + self.dy * self.dy)
            tip_speed = 10
        else:
            speed = abs(self.dx)
            tip_speed = 5

        # below half tip_speed, sprite rotation is always zero
        if speed < tip_speed / 2:
            return 0

        # calculate direction the bird is heading in
        heading = atan2(self.dy, abs(self.dx))
        if self.facing == RIGHT:
            heading *= -1

        # up to tip_speed, sprite rotates towards heading somewhat
        if speed < tip_speed:

            ratio = speed * 2 / tip_speed - 1
            return heading * ratio

        # above tip_speed, sprite always faces in direction of bird's motion
        return heading


    def update(self):
        WorldItem.update(self)
        self.actions = self.think()
        self.act()
        self.choose_frame()
        if self.last_flap is not None:
            self.last_flap += 1
        self.rotation = self.sprite_rotation()


    @staticmethod
    def bounce(one, two):
        '''
        perfect elastic collision between bodies one and two, described at:
        http://www.gamasutra.com/view/feature/3015/
            pool_hall_lessons_fast_accurate_.php
        '''
        # masses
        m1 = m2 = 1

        # offset of body two from body one
        offset = Vec2(two.x, two.y) - Vec2(one.x, one.y)
        offsetn = offset.normalized()

        # velocities
        v1 = Vec2(one.dx, one.dy)
        v2 = Vec2(two.dx, two.dy)

        # momentum exchanged
        delta_p = 2 * (v1.dot(offsetn)- v2.dot(offsetn)) * offsetn / (m1 + m2)

        # accelerations
        a1 = delta_p * m2
        one.ddx -= a1.x
        one.ddy -= a1.y

        a2 = delta_p * m1
        two.ddx += a2.x
        two.ddy += a2.y


    def die(self):
        self.is_alive = False
        self.can_fall_off = True

