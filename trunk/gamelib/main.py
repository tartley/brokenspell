
from os.path import join

from pyglet import app, clock
from pyglet.window import Window
from pyglet.media import load


def main():
    music = load(join('data', 'musik.ogg'))
    win = Window()
    clock.schedule_once(lambda _: music.play, 1)
    app.run()

