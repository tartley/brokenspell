
from pyglet import clock
from pyglet.gl import (
    glBlendFunc, glEnable, glColor3ub,
    GL_BLEND, GL_ONE_MINUS_SRC_ALPHA, GL_SRC_ALPHA,
)
from pyglet.graphics import Batch, OrderedGroup

from enemy import Enemy
from feather import Feather
from graphics import Graphics
from ground import Ground
from hudpoints import HudPoints
from player import Player


class Render(object):

    groups = [
        OrderedGroup(0), # sky
        OrderedGroup(1), # hills
        OrderedGroup(2), # birds & feathers
        OrderedGroup(3), # hud
    ]

    def __init__(self, arena):
        self.arena = arena

        arena.item_added += self.on_add_item
        arena.item_removed += self.on_remove_item

        self.clockDisplay = clock.ClockDisplay()
        self.batch = Batch()


    def assign_images_and_sizes(self, images):
        for klass in [Ground, Player, Enemy, Feather]:
            klass.images = images[klass.__name__]
            klass.width = klass.images[0].width
            klass.height = klass.images[0].height


    def init(self, win):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        graphics = Graphics()
        images = graphics.load()
        self.assign_images_and_sizes(images)
        HudPoints.create_images()

        win.on_draw = self.draw


    def draw(self):
        # TODO, can this be over items[SpriteItem] or something, and
        # hence drop the hasattr check?
        for item in self.arena.items:
            if hasattr(item, 'animate'):
                item.animate()

        self.batch.draw()
        self.clockDisplay.draw()


    def on_add_item(self, _, item):
        item.add_to_batch(self.batch, self.groups)


    def on_remove_item(self, _, item):
        item.remove_from_batch(self.batch)

