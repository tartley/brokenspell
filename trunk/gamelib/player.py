
from pyglet import resource
from pyglet.sprite import Sprite
from pyglet.window import key


GRAVITY = 0.4
LEFT, RIGHT = 0, 1


class Player(object):

    def __init__(self):
        self.age = 0.0
        self.x = self.y = 0
        self.dx = self.dy = 5
        self.can_flap = True
        self.facing = RIGHT

        self.sprites= {}
        self.sprites[LEFT] = \
            Sprite(resource.image('data/images/Player-flap-L.png'))
        self.sprites[RIGHT] = \
            Sprite(resource.image('data/images/Player-flap-R.png'))


    def read_controls(self, keyhandler):
        if keyhandler[key.Z]:
            flapping = self.try_flap()
        else:
            self.can_flap = True
            flapping = False

        ddx = 0.3
        if flapping:
            ddx = 6

        if keyhandler[key.LEFT]:
            self.dx -= ddx
            self.facing = LEFT
        if keyhandler[key.RIGHT]:
            self.dx += ddx
            self.facing = RIGHT


    def try_flap(self):
        if self.can_flap:
            self.dy += 7
            self.can_flap = False
            return True
        return False


    def update(self, dt):
        self.age += dt
        self.dy -= GRAVITY
        self.dx *= 0.9
        self.x += self.dx
        self.y += self.dy
        if self.y < 0:
            self.y = 0
            self.dy *= -0.5


    def draw(self):
        sprite = self.sprites[self.facing]
        sprite.position = (self.x, self.y)
        sprite.draw()

