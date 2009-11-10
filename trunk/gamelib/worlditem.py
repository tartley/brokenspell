
from math import degrees

from gameitem import GameItem


GRAVITY = 0.2
LEFT, RIGHT = 'L', 'R'


class WorldItem(GameItem):

    AIR_RESIST_X = 0.98
    AIR_RESIST_Y = 0.98

    can_fall_off = False

    is_player = False
    is_enemy = False
    is_feather = False

    render_layer = 2

    def __init__(self, x=0, y=0, dx=0, dy=0):
        GameItem.__init__(self)
        WorldItem.reincarnate(self, x, y, dx, dy)
        self.sprite = None
        self.frame_idx = 0
        self.width = 0
        self.height = 0


    def __str__(self):
        return "<%s%s>" % (type(self).__name__, self.id)


    def reincarnate(self, x, y, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ddx = 0
        self.ddy = 0
        self.rotation = 0
        self.remove_from_game = False


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


    def animate(self, images):
        self.sprite._x = self.x
        self.sprite._y = self.y
        self.sprite._rotation = degrees(self.rotation)
        self.sprite.image = images[self.__class__.__name__][self.frame_idx]
        self.sprite._update_position()


    def collided_with(self, other):
        self.ddx += other.dx - self.dx
        self.ddy += other.dy - self.dy
        if self.y < other.y:
            self.y -= 2
        if self.x < other.x:
            self.x -= 2

