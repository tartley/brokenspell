
import pyglet
from pyglet.window import key, Window

from config import settings
from game import Game
from sounds import load as load_sounds
from music import Music
from render import Render


class Application(object):

    def __init__(self):
        self.win = None
        self.music = None
        self.vsync = True
        if (
            settings.has_option('all', 'vsync') and
            not settings.getboolean('all', 'vsync')
        ):
            self.vsync = False


    def launch(self):
        self.win = Window(
            width=1024, height=768, vsync=self.vsync, visible=False)
        self.win.set_mouse_visible(False)

        self.win.push_handlers(self)

        game = Game(self.win)
        render = Render(game)
        render.init(self.win)
        game.init()

        load_sounds()

        self.music = Music()
        self.music.load()
        self.music.play()

        self.win.set_visible()
        pyglet.app.run()


    def on_key_press(self, symbol, _):
        if symbol == key.M:
            self.music.toggle()
        elif symbol == key.ESCAPE:
            self.win.has_exit = True
        elif symbol == key.F4:
            self.vsync = not self.vsync
            self.win.set_vsync(self.vsync)

