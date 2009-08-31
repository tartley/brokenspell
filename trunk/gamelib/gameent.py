

GRAVITY = 0.4
LEFT, RIGHT = 'L', 'R'


class GameEnt(object):

    SPRITE_PREFIX = None

    AIR_RESIST_X = 0.95
    AIR_RESIST_Y = 0.95

    def __init__(self, x, y, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.is_gone = False


    def update(self):
        self.dy -= GRAVITY
        self.dx *= self.AIR_RESIST_X
        self.dy *= self.AIR_RESIST_Y

        self.x += self.dx
        self.y += self.dy
        if self.y < 0:
            self.y = 0
            self.dy *= -0.5


    def draw(self):
        sprite = self.get_sprite()
        sprite.position = (self.x, self.y)
        sprite.draw()

    
    def collided_with(self, ent):
        pass


    def update_sprite_stats(self, sprite):
        self.center_x = sprite.width/2
        self.center_y = sprite.height/2
        self.width = sprite.width
        self.height = sprite.height
