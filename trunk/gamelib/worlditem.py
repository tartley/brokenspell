
from spriteitem import SpriteItem


GRAVITY = 0.2
LEFT, RIGHT = 'L', 'R'


class WorldItem(SpriteItem):

    AIR_RESIST_X = 0.98
    AIR_RESIST_Y = 0.98

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
        self.dx = (self.dx + self.ddx) * self.AIR_RESIST_X
        self.dy = (self.dy + self.ddy - GRAVITY) * self.AIR_RESIST_Y
        self.ddx = 0
        self.ddy = 0

        self.x += self.dx
        self.y += self.dy

        if self.can_fall_off:
            if self.y < -self.height / 2:
                self.remove_from_game = True
        else:
            if self.y < self.height / 2:
                self.y = self.height / 2
                self.dy = abs(self.dy) * 0.5


    def wraparound(self, width):
        if self.x < self.width:
            self.x += width + self.width
        if self.x > width:
            self.x -= width + self.width


    def collided_with(self, other):
        self.ddx += other.dx - self.dx
        self.ddy += other.dy - self.dy
        if self.y < other.y:
            self.y -= 2
        if self.x < other.x:
            self.x -= 2

