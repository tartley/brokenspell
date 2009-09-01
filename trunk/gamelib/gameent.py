

GRAVITY = 0.2
LEFT, RIGHT = 'L', 'R'


class GameEnt(object):

    next_id = 0

    SPRITE_PREFIX = None

    AIR_RESIST_X = 0.98
    AIR_RESIST_Y = 0.98

    can_fall_off = False
    level = None

    def __init__(self, x, y, dx=0, dy=0):
        self.id = GameEnt.next_id
        GameEnt.next_id += 1
        GameEnt.reincarnate(self, x, y, dx, dy)
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
        self.remove_from_game = False
        self.born = self.level.age


    def get_age(self):
        return self.level.age - self.born


    def update(self):
        self.dx += self.ddx
        self.dy += self.ddy - GRAVITY
        self.dx *= self.AIR_RESIST_X
        self.dy *= self.AIR_RESIST_Y

        self.ddx = 0
        self.ddy = 0

        self.x += self.dx
        self.y += self.dy
        
        if self.can_fall_off:
            if self.y < -self.height:
                self.remove_from_game = True
        else:
            if self.y < 0:
                self.y = 0
                self.dy *= -0.5


    def draw(self):
        sprite = self.get_sprite()
        sprite.position = (self.x, self.y)
        sprite.draw()

    
    def collided_with(self, other):
        self.ddx += other.dx - self.dx
        self.ddy += other.dy - self.dy


    def update_sprite_stats(self, sprite):
        self.center_x = sprite.width/2
        self.center_y = sprite.height/2
        self.width = sprite.width
        self.height = sprite.height

