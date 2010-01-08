
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
from player import Player


class Render(object):

    groups = [
        OrderedGroup(0), # sky
        OrderedGroup(1), # hills
        OrderedGroup(2), # birds & feathers
        OrderedGroup(3), # hud
    ]

    def __init__(self, game):
        self.game = game
        game.item_added += self.on_add_item
        game.item_removed += self.on_remove_item

        self.win = None

        self.clockDisplay = clock.ClockDisplay()
        self.batch = Batch()


    def assign_images_and_sizes(self, images):
        for klass in [Ground, Player, Enemy, Feather]:
            klass.images = images[klass.__name__]
            klass.width = klass.images[0].width
            klass.height = klass.images[0].height


    def init(self, win):
        self.win = win
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        graphics = Graphics()
        images = graphics.load()
        self.assign_images_and_sizes(images)

        win.on_draw = self.draw


    def draw(self):
        for item in self.game:
            if hasattr(item, 'animate'):
                item.animate()

        self.batch.draw()
        self.clockDisplay.draw()

        self.win.invalid = False


    def on_add_item(self, item):
        if hasattr(item, 'add_to_batch'):
            item.add_to_batch(self.batch, self.groups)


    def on_remove_item(self, item):
        if hasattr(item, 'remove_from_batch'):
            item.remove_from_batch(self.batch)

