
from pyglet import app
from pyglet.window import Window
from pyglet.media import load


def main():
    music = load('data/m3d049_bopMix_03_hwyChipmusik_by_xik.ogg')
    win = Window()
    music.play()
    app.run()

