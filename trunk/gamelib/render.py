
from pyglet import clock
from pyglet.gl import (
    glBlendFunc, glEnable,
    GL_BLEND, GL_ONE_MINUS_SRC_ALPHA, GL_QUADS, GL_SRC_ALPHA,
)
from pyglet.graphics import Batch, draw as pyglet_draw
from pyglet.text import Label

from gameent import GameEnt
from graphics import Graphics


class Render(object):

    # TODO: we don't need to pass application or win here
    # just world would be fine
    # uses of win in clear will go away when background is a gameent
    def __init__(self, application, win):
        self.application = application
        self.win = win

        self.application.world.item_added += self.add_sprite_to_batch
        self.application.world.item_removed += self.remove_sprite_from_batch

        self.clockDisplay = clock.ClockDisplay()
        self.ground = None
        self.batch = Batch()


    def init(self, win):
        self.graphics = Graphics()
        self.graphics.load()

        self.score_label = Label("0",
            font_size=36, x=win.width, y=win.height,
            anchor_x='right', anchor_y='top')

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    def clear(self):
        verts = (
            self.win.width, self.win.height,
            0, self.win.height,
            0, 0,
            self.win.width, 0,
        )
        colors = (
            000, 000, 127,
            000, 000, 127,
            064, 127, 255,
            064, 127, 255,
        )
        pyglet_draw(len(verts) / 2, GL_QUADS,
            ('v2f', verts),
            ('c3B', colors),
        )


    def draw(self):
        self.clear()
        self.graphics.images['Ground'].blit(0, 0)
        self.application.user_message.draw()
        self.application.instructions.draw()
        self.score_label.text = '%d' % self.application.game.score
        self.score_label.draw()
        self.clockDisplay.draw()
        for ent in self.application.world.ents:
            ent.animate(self.graphics.images)
        self.batch.draw()


    def add_sprite_to_batch(self, _, item):
        item.sprite.batch = self.batch


    def remove_sprite_from_batch(self, _, item):
        item.sprite.batch = None

