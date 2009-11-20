
from math import degrees

from pyglet.sprite import Sprite

from gameitem import GameItem


class SpriteItem(GameItem):
    '''GameItem that is rendered as a single sprite'''

    images = None
    render_layer = 2 # birds and feathers


    def __init__(self, x=0, y=0):
        GameItem.__init__(self)
        self.x = x
        self.y = y
        self.rotation = 0

        self.sprite = None
        self.frame_idx = 0


    def add_to_batch(self, batch, groups):
        self.sprite = Sprite(
            self.images[self.frame_idx],
            batch=batch,
            group=groups[self.render_layer] )


    def remove_from_batch(self, batch):
        self.sprite.batch = None
        self.sprite.delete()


    def animate(self):
        self.sprite._x = self.x
        self.sprite._y = self.y
        self.sprite._rotation = degrees(self.rotation)
        image = self.images[self.frame_idx]
        if self.sprite.image != image:
            self.sprite.image = image
        else:
            self.sprite._update_position()

