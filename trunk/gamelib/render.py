
from pyglet import clock
from pyglet.gl import (
    glBlendFunc, glEnable,
    GL_BLEND, GL_ONE_MINUS_SRC_ALPHA, GL_QUADS, GL_SRC_ALPHA,
)
from pyglet.graphics import draw
from pyglet.text import Label

from gameent import GameEnt
from graphics import Graphics, load_sprite_images


class Render(object):

    def __init__(self, application):
        self.application = application
        application.win.on_draw = self.draw
        self.clockDisplay = clock.ClockDisplay()
        self.ground = None


    def init(self):
        self.graphics = Graphics()
        self.graphics.load()
        # TODO: delete this, use spritesheet instead
        GameEnt.sprite_images = load_sprite_images()

        win = self.application.win
        self.score_label = Label("0",
                font_size=36, x=win.width, y=win.height,
                anchor_x='right', anchor_y='top')

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    def clear(self):
        win = self.application.win
        verts = (
            win.width, win.height,
            0, win.height,
            0, 0,
            win.width, 0,
        )
        colors = (
            000, 000, 127,
            000, 000, 127,
            064, 127, 255,
            064, 127, 255,
        )
        draw(len(verts) / 2, GL_QUADS,
            ('v2f', verts),
            ('c3B', colors),
        )


    def draw(self):
        self.clear()
        self.graphics.ground.blit(0, 0)
        self.application.user_message.draw()
        self.application.instructions.draw()
        self.score_label.text = '%d' % self.application.game.score
        self.score_label.draw()
        self.clockDisplay.draw()
        for ent in self.application.world.ents:
            ent.animate()
            ent.draw()

