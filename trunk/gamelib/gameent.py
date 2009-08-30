
GRAVITY = 0.6
LEFT, RIGHT = 0, 1


class GameEnt(object):

    def __init__(self, x, y, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        if dx < 0:
            self.facing = LEFT
        else:
            self.facing = RIGHT
        self.sprites= {}


    def update(self):
        self.dy -= GRAVITY
        self.dx *= 0.95
        self.dy *= 0.95
        self.x += self.dx
        self.y += self.dy
        if self.y < 0:
            self.y = 0
            self.dy *= -0.5


    def get_sprite(self):
        return self.sprites[self.facing]


    def draw(self):
        sprite = self.get_sprite()
        sprite.position = (self.x, self.y)
        sprite.draw()

