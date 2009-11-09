
from pyglet.graphics import OrderedGroup
from pyglet.sprite import Sprite

from gameitem import GameItem


group = OrderedGroup(1)


class Ground(GameItem):

    def __init__(self, images):
        self.sprite = Sprite(images['Ground'], group=group)
        self.sprite.position = 0, 0

