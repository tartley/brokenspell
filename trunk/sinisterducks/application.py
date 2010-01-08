
import pyglet
from pyglet.window import key, Window

from .config import settings
from .game import Game
from .gameitem import GameItem
from .sounds import load as load_sounds
from .music import Music
from .render import Render


class KeyHandler(GameItem):

    def __init__(self, handlers):
        GameItem.__init__(self)
        self.handlers = handlers

    def on_key_press(self, symbol, _):
        if symbol in self.handlers:
            self.handlers[symbol]()



class Application(object):

    def __init__(self):
        self.win = None
        self.music = None
        self.vsync = (
            not settings.has_option('all', 'vsync') or
            settings.getboolean('all', 'vsync')
        )


    def launch(self):
        self.win = Window(
            width=1024, height=768, vsync=self.vsync, visible=False)
        self.win.set_mouse_visible(False)
        GameItem.win = self.win

        load_sounds()

        self.music = Music()
        self.music.load()
        self.music.play()

        keystate = key.KeyStateHandler()
        self.win.push_handlers(keystate)

        game = Game(keystate, self.win.width, self.win.height)

        handlers = {
            key.M: self.toggle_music,
            key.F4: self.toggle_vsync,
            key.ESCAPE: self.exit,
        }
        game.add(KeyHandler(handlers))

        render = Render(game)
        render.init(self.win)
        game.startup(self.win)
        self.win.set_visible()
        pyglet.app.run()


    def toggle_vsync(self):
        self.vsync = not self.vsync
        self.win.set_vsync(self.vsync)

    def toggle_music(self):
        self.music.toggle()

    def exit(self):
        self.win.has_exit = True

