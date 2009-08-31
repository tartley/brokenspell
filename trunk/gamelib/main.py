
from os.path import join
from random import randint, uniform

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


class Application(object):

    def __init__(self):
        self.win = Window(width=1024, height=768)
        self.win.set_exclusive_mouse()
        self.win.on_draw = self.draw

        self.keyhandler = key.KeyStateHandler()
        self.win.push_handlers(self.keyhandler)

        self.player_dead = False
        self.user_message = UserMessage(self.win.width,
                                        self.win.height)
        self.level = Level(self.win.width, self.win.height)
        self.player = Player(self.keyhandler,
            self.level.width / 2, self.level.height)
        self.level.add_player(self.player)
        clock.schedule_once(lambda _: self.add_enemy(), 2)
        self.instructions = Instructions()

        # music = load(join('data', 'musik.ogg'))
        # clock.schedule_once(lambda _: music.play(), 1)
        clock.schedule(self.update)


    def add_enemy(self):
        x = uniform(0, self.level.width)
        y = self.level.height
        dx = uniform(-20, 20)
        dy = uniform(0, 10)
        feathers = randint(1, 5)
        self.level.add(Enemy(x, y, dx=dx, dy=dy, feathers=feathers))
        clock.schedule_once(lambda _: self.add_enemy(), uniform(4, 8))


    def update(self, dt):
        if self.level.update(dt) and not self.player_dead:
            self.player_dead = True
            self.user_message.set_message('Oh no! Get ready...')
            clock.schedule_once(lambda _: self.reincarnate(), 2)


    def reincarnate(self):
        self.user_message.set_message(None)
        self.level.reset_player()
        self.player_dead = False


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
