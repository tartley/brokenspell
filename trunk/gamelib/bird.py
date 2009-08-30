
from glob import glob

from pyglet import resource
from pyglet.sprite import Sprite

from gameent import GameEnt, LEFT, RIGHT


GLIDE_STEER = 0.3
FLAP_STEER = 6
FLAP_LIFT = 13


class Action(object):
    FLAP = 0
    LEFT = 1
    RIGHT = 2


class Bird(GameEnt):

    def __init__(self, x, y, dx=0, dy=0):
        GameEnt.__init__(self, x, y, dx, dy)
        self.can_flap = True
        self.last_flap = None
        if dx < 0:
            self.facing = LEFT
        else:
            self.facing = RIGHT
        self.sprites = self.load_sprites()
        self.get_sprite()
        self.is_enemy = True


    def act(self, actions):
        if Action.FLAP in actions:
            if self.can_flap:
                self.flap()
        else:
            self.can_flap = True

        ddx = GLIDE_STEER
        if self.last_flap == 0:
            ddx = FLAP_STEER

        if Action.LEFT in actions:
            self.dx -= ddx
            self.facing = LEFT
        if Action.RIGHT in actions:
            self.dx += ddx
            self.facing = RIGHT


    def flap(self):
        self.dy += FLAP_LIFT
        self.last_flap = 0
        self.can_flap = False


    def update(self):
        GameEnt.update(self)
        actions = self.think()
        self.act(actions)
        if self.last_flap is not None:
            self.last_flap += 1 


    def get_sprite(self):
        action = 'flight'
        if self.last_flap is not None and self.last_flap < 5:
            action = 'flap'
        sprite = self.sprites['%s-%s' % (action, self.facing,)]
        self.update_sprite_stats(sprite)
        return sprite


    def load_sprites(self):
        sprites = {}
        files = glob('%s*' % (self.SPRITE_PREFIX,))
        for file in files:
            file = file.replace('\\', '/')
            image = resource.image(file)
            name = file[len(self.SPRITE_PREFIX):-4]
            sprites[name] = Sprite(image)
        return sprites

