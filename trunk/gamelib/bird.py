
from glob import glob
from random import uniform

from pyglet import resource
from pyglet.sprite import Sprite

from feather import Feather
from gameent import GameEnt, LEFT, RIGHT


GLIDE_STEER = 0.1
FLAP_STEER = 3
FLAP_LIFT = 5


class Action(object):
    FLAP = 0
    LEFT = 1
    RIGHT = 2


class Bird(GameEnt):

    def __init__(self, x, y, dx=0, dy=0, feathers=3):
        GameEnt.__init__(self, x, y, dx, dy)
        self.feathers = feathers
        self.can_flap = True
        self.last_flap = None
        if dx < 0:
            self.facing = LEFT
        else:
            self.facing = RIGHT
        self.sprites = self.load_sprites()
        self.is_alive = True
        self.actions = set()


    def act(self):
        if Action.FLAP in self.actions:
            if self.can_flap:
                self.dy += FLAP_LIFT
                self.last_flap = 0
                self.can_flap = False
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


    def update(self):
        GameEnt.update(self)
        self.actions = self.think()
        self.act()
        if self.last_flap is not None:
            self.last_flap += 1


    def lose_feather(self, otherx, othery):
        print 'losefeather', type(self).__name__
        self.feathers -= 1
        if self.feathers >= 0:
            directionx = self.x - otherx
            directiony = self.y - othery
            feather = Feather(
                self.x + directionx, self.y + directiony,
                self.dx + directionx / 3.0, self.dy + directiony / 5.0,
                owner=self)
            self.level.add(feather)
        else:
            self.is_alive = False
            self.can_fall_off = True
            self.think = lambda: set()


    def collided_with(self, other):
        if self.is_alive:
            if isinstance(other, Bird):
                GameEnt.collided_with(self, other)
                if other.is_alive and self.y < other.y:
                    self.lose_feather(other.x, other.y)
            elif isinstance(other, Feather) and other.owner is not self:
                other.is_gone = True
                self.feathers += 1


    def get_sprite(self):
        action = 'flight' if self.is_alive else 'dead'
        flapping = (
            self.is_alive and (
                (self.last_flap is not None
                 and self.last_flap < 5)
                or Action.FLAP in self.actions)
        )
        if flapping:
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

