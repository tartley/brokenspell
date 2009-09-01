
from os.path import join

from pyglet import app, clock
from pyglet.event import EVENT_HANDLED
from pyglet.gl import (
    glClearColor, glClear, glLoadIdentity, glMatrixMode, gluOrtho2D, 
    GL_COLOR_BUFFER_BIT, GL_PROJECTION, GL_QUADS, 
)
from pyglet.graphics import draw
from pyglet.window import key, Window
from pyglet.media import load

from enemy import Enemy
from instructions import Instructions
from player import Player
from level import Level
from user_message import UserMessage


clockDisplay = clock.ClockDisplay()

MESSAGES = [
        "Sinister Ducks",
        "ESC to exit",
        "Left and right to move around",
        "Z flaps wings",
        "Catch feathers to increase flap strength",
        None
]


class Application(object):

    def __init__(self):
        self.win = Window(width=1024, height=768)
        self.win.set_exclusive_mouse()
        self.win.on_draw = self.draw

        music = load(join('data', 'music2.mp3'))
        clock.schedule_once(lambda _: music.play(), 1)

        self.keyhandler = key.KeyStateHandler()
        self.win.push_handlers(self.keyhandler)

        self.level = Level(self.win.width, self.win.height)
        self.player = Player(
            self.keyhandler,
            self.level.width / 2, self.level.height)
        self.resurrecting = False
        self.user_message = UserMessage(self.win.width,
                                        self.win.height)
        self.instructions = Instructions(
            MESSAGES, self.win.width, 0, 'right', 'top')

        clock.schedule_once(
            lambda _: self.level.spawn_enemy(8, self.player),
            00.25)
        clock.schedule(self.update)
        self.get_ready()


    def get_ready(self):
        self.player.reincarnate(self.level.width / 2, self.level.height)
        self.user_message.set_message('Get ready...')
        clock.schedule_once(lambda _: self.spawn_player(), 1)


    def spawn_player(self):
        self.level.add(self.player)
        self.user_message.set_message(None)
        self.resurrecting = False


    def update(self, dt):
        self.level.update(dt)
        if not self.player.is_alive and not self.resurrecting:
            self.resurrecting = True
            self.user_message.set_message('Oh no!')
            clock.schedule_once(lambda _: self.get_ready(), 2)


    def draw(self):
        self.gradient_clear()
        self.level.draw()
        self.instructions.draw()
        clockDisplay.draw()
        self.user_message.draw()


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


def main():
    application = Application()
    app.run()

