
from math import atan2

from spriteitem import SpriteItem
from vec2 import Vec2


GRAVITY = 0.2
LEFT, RIGHT = 'L', 'R'


class WorldItem(SpriteItem):

    AIR_RESIST = 0.98

    is_player = False
    is_enemy = False
    is_feather = False
    can_fall_off = False


    def __init__(self, x=0, y=0, dx=0, dy=0):
        SpriteItem.__init__(self, x, y)
        self.dx = dx
        self.dy = dy
        self.ddx = 0
        self.ddy = 0


    def update(self):
        self.dx += self.ddx
        self.dx *= self.AIR_RESIST
        self.dy += self.ddy - GRAVITY
        self.dy *= self.AIR_RESIST
        self.ddx = 0
        self.ddy = 0
        self.x += self.dx
        self.y += self.dy
        self.test_for_fall_off_screen()


    def test_for_fall_off_screen(self):
        if self.can_fall_off:
            if self.y < -self.height / 2:
                self.remove_from_game = True
        else:
            if self.y < self.height / 2:
                self.y = self.height / 2
                self.dy = abs(self.dy) * 0.5


    def collided_with(self, other):
        pass


    # TODO: make collisions detection stop detecting each collision after the
    # first impact, until the two items have un-collided again.
    # TODO: make collision detection call this function once per collision
    # (not once per worlditem), so we can apply all this to both items
    # together.
    @staticmethod
    def bounce(one, two):
        '''
        perfect elastic collision between bodies one and two, described at:
        http://www.gamasutra.com/view/feature/3015/pool_hall_lessons_fast_accurate_.php
        '''
        # masses
        m1 = m2 = 1

        # offset of body two from body one
        offset = Vec2(two.x, two.y) - Vec2(one.x, one.y)
        n = offset.normalized()

        # velocities
        v1 = Vec2(one.dx, one.dy)
        v2 = Vec2(two.dx, two.dy)

        # momentum exchanged
        delta_p = 2 * (v1.dot(n)- v2.dot(n)) * n / (m1 + m2)

        # acceleration
        a1 = delta_p * m2
        one.ddx -= a1.x
        one.ddy -= a1.y

