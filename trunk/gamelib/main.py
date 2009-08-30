
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

from player import Player
from level import Level

MESSAGES = [
        "ESC to exit",
        "Left and right to move around",
        "Z flaps wings",
        "Catch feathers to increase flap strength",
        ""
]

clockDisplay = clock.ClockDisplay()


class Application(object):

    def __init__(self):
        self.player = Player()
        self.level = Level(self.player)
        self.win = None
        self.keyhandler = None
        self.label = None
        self.showing_message = 0


    def update(self, dt):
        self.player.read_controls(self.keyhandler)
        self.level.update(dt)


    def draw(self):
        self.gradient_clear()
        self.level.draw()
        if self.label:
            self.label.draw()
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

    def change_text(self):
        message = MESSAGES[self.showing_message]
        self.showing_message += 1
        print "Label", message
        self.label = Label(message,
                font_size=36, x=1024, y=0,
                anchor_x='right', anchor_y='bottom')



    def run(self):
        self.win = Window(width=1024, height=728)
        self.win.set_exclusive_mouse()
        self.win.on_draw = self.draw

        self.keyhandler = key.KeyStateHandler()
        self.win.push_handlers(self.keyhandler)

        # music = load(join('data', 'musik.ogg'))
        # clock.schedule_once(lambda _: music.play(), 1)
        clock.schedule(self.update)
        for number, message in enumerate(MESSAGES):
            clock.schedule_once(lambda _: self.change_text(), 3*number)
        app.run()


def main():
    application = Application()
    application.run()

