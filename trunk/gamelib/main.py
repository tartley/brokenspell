
from os.path import join

from pyglet import app, clock
from pyglet.event import EVENT_HANDLED
from pyglet.gl import (
    glClearColor, glClear, glLoadIdentity, glMatrixMode, gluOrtho2D, 
    GL_COLOR_BUFFER_BIT, GL_PROJECTION, GL_QUADS, 
)
from pyglet.graphics import draw
from pyglet.text import Label
from pyglet.window import key, Window
from pyglet.media import load

from instructions import Instructions
from player import Player
from level import Level


clockDisplay = clock.ClockDisplay()


class Application(object):

    def __init__(self):
        self.player = Player()
        self.level = Level(self.player)
        self.instructions = Instructions()
        self.win = None
        self.keyhandler = None


    def update(self, dt):
        self.player.read_controls(self.keyhandler)
        self.level.update(dt)


    def draw(self):
        self.gradient_clear()
        self.level.draw()
        self.instructions.draw()
        clockDisplay.draw()


    def gradient_clear(self):
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
        draw(len(verts) / 2, GL_QUADS,
            ('v2f', verts),
            ('c3B', colors),
        )        


    def run(self):
        self.win = Window(width=1024, height=728)
        self.win.set_exclusive_mouse()
        self.win.on_draw = self.draw

        self.keyhandler = key.KeyStateHandler()
        self.win.push_handlers(self.keyhandler)

        # music = load(join('data', 'musik.ogg'))
        # clock.schedule_once(lambda _: music.play(), 1)
        clock.schedule(self.update)
        app.run()


def main():
    application = Application()
    application.run()

