
from glob import glob
from pyglet import resource
from pyglet.sprite import Sprite

GRAVITY = 0.6
LEFT, RIGHT = 'L', 'R'


class GameEnt(object):

    SPRITE_PREFIX = None

    def __init__(self, x, y, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        if dx < 0:
            self.facing = LEFT
        else:
            self.facing = RIGHT
        self.sprites = self.load_sprites()


    def load_sprites(self):
        sprites = {}
        files = glob('%s*' % (self.SPRITE_PREFIX,))
        for file in files:
            file = file.replace('\\', '/')
            image = resource.image(file)
            name = file[len(self.SPRITE_PREFIX):-4]
            sprites[name] = Sprite(image)
        return sprites


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
        action = 'flight'
        if self.last_flap < 5:
            action = 'flap'
        sprite = self.sprites['%s-%s' % (action, self.facing,)]
        self.center_x = sprite.width/2
        self.center_y = sprite.height/2
        self.width = sprite.width
        self.height = sprite.height
        return sprite


    def draw(self):
        sprite = self.get_sprite()
        sprite.position = (self.x, self.y)
        sprite.draw()

    
    def collided_with(self, ent):
        pass
