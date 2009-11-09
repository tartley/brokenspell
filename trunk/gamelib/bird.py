
from glob import glob

from pyglet import resource
from pyglet.sprite import Sprite

from behaviour import Action
from feather import Feather
from worlditem import WorldItem, LEFT, RIGHT
from sounds import play


GLIDE_STEER = 0.1
FLAP_STEER = 3
FLAP_LIFT = 5


class Bird(WorldItem):

    def __init__(self, x, y, dx=0, dy=0, feathers=3):
        WorldItem.__init__(self, x, y, dx, dy)
        self.feathers = feathers
        if self.dx < 0:
            self.facing = LEFT
        else:
            self.facing = RIGHT
        self.can_flap = True
        self.last_flap = None
        self.is_alive = True
        self.actions = set()
        self.foe = None
        self.update_sprite_stats()


    def reincarnate(self, x, y, feathers=3):
        WorldItem.reincarnate(self, x, y)
        self.feathers = feathers
        self.can_fall_off = False


    def act(self):
        if Action.FLAP in self.actions:
            if self.can_flap:
                self.dy += FLAP_LIFT
                self.last_flap = 0
                self.can_flap = False
                if self.is_player:
                    play('flap')
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


    def choose_frame(self):
        self.frame_idx = 0
        if self.facing == RIGHT:
            self.frame_idx += 1
        if self.is_alive:
            if Action.FLAP in self.actions:
                self.frame_idx += 2
        else:
            self.frame_idx += 4


    def update(self):
        WorldItem.update(self)
        self.actions = self.think()
        self.act()
        self.choose_frame()
        if self.last_flap is not None:
            self.last_flap += 1
        self.rotation = -self.dx * self.dy / 100.0


    def lose_feather(self, otherx, othery):
        self.feathers -= 1
        dx, dy = self.get_collision_opposite(otherx, othery)
        feather = Feather(
            self.x, self.y,
            dx, dy,
            self)
        self.arena.add(feather)

        if self.feathers == 0:
            self.die()


    def get_collision_opposite(self, otherx, othery):
        directionx = self.x - otherx
        directiony = self.y - othery
        return self.dx + directionx / 3.0, self.dy + directiony / 5.0


    def die(self):
        self.is_alive = False
        self.can_fall_off = True


    def collided_with(self, other):
        if self.is_alive:
            if other.is_player or other.is_enemy:
                if other.is_alive:
                    WorldItem.collided_with(self, other)
                    if self.y < other.y:
                        self.foe = other
                        if other.is_enemy != self.is_enemy:
                            self.lose_feather(other.x, other.y)
            elif other.is_feather and other.owner is not self:
                other.remove_from_game = True
                self.feathers += 1

