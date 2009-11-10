
from pyglet.sprite import Sprite

from gameitem import GameItem


class Ground(GameItem):

    render_layer = 1

    def __init__(self):
        GameItem.__init__(self)
        self.sprite = None


    # TODO: these method are identical to those in WorldItem
    # Is GameItem a WorldItem? Or some other tweak to the inheritance?
    def add_to_batch(self, batch, groups, images):
        self.sprite = Sprite(
            images[self.__class__.__name__][0],
            batch=batch,
            group=groups[self.render_layer] )
        self.update_sprite_stats()


    def remove_from_batch(self, batch):
        self.sprite.batch = None
        self.sprite.delete()


