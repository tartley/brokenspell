
from pyglet import clock
from pyglet.gl import (
    glBlendFunc, glEnable,
    GL_BLEND, GL_ONE_MINUS_SRC_ALPHA, GL_QUADS, GL_SRC_ALPHA,
)
from pyglet.graphics import draw


class Render(object):

    def __init__(self, application):
        self.application = application
        application.win.on_draw = self.draw
        self.clockDisplay = clock.ClockDisplay()


    def init(self):
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
        self.application.level.draw()
        self.application.user_message.draw()
        self.application.instructions.draw()
        self.application.meter.draw()
        self.clockDisplay.draw()

