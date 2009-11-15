
from pyglet import clock
from pyglet.gl import (
    glBlendFunc, glEnable,
    GL_BLEND, GL_ONE_MINUS_SRC_ALPHA, GL_SRC_ALPHA,
)
from pyglet.graphics import Batch, OrderedGroup

from graphics import Graphics


class Render(object):

    groups = [
        OrderedGroup(0), # sky
        OrderedGroup(1), # hills
        OrderedGroup(2), # birds & feathers
        OrderedGroup(3), # hud
    ]

    def __init__(self, arena):
        self.arena = arena
        self.images = None

        arena.item_added += self.on_add_item
        arena.item_removed += self.on_remove_item

        self.clockDisplay = clock.ClockDisplay()
        self.batch = Batch()


    def init(self, win):
        graphics = Graphics()
        self.images = graphics.load()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        win.on_draw = self.draw


    def draw(self):
        # TODO: move this to update instead of draw
        for item in self.arena.items:
            if hasattr(item, 'animate'):
                item.animate(self.images)

        self.batch.draw()

        self.clockDisplay.draw()


    def on_add_item(self, _, item):
        item.add_to_batch(self.batch, self.groups, self.images)


    def on_remove_item(self, _, item):
        item.remove_from_batch(self.batch)

