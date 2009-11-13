
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

    # TODO: we don't need to pass application or win here
    # just arena would be fine
    def __init__(self, application, win):
        self.application = application
        self.win = win
        self.images = None

        self.application.arena.item_added += self.add_item_to_batch
        self.application.arena.item_removed += self.remove_item_from_batch

        self.clockDisplay = clock.ClockDisplay()
        self.batch = Batch()


    def init(self, win):
        graphics = Graphics()
        self.images = graphics.load()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    def draw(self):
        for item in self.application.arena.items:
            if hasattr(item, 'animate'):
                item.animate(self.images)

        self.batch.draw()

        self.clockDisplay.draw()


    def add_item_to_batch(self, _, item):
        item.add_to_batch(self.batch, self.groups, self.images)


    def remove_item_from_batch(self, _, item):
        item.remove_from_batch(self.batch)

