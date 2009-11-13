
from pyglet import app, clock
from pyglet.window import key, Window

from arena import Arena
from config import settings
from game import Game
from gameitem import GameItem
from music import Music
from render import Render


class Application(object):

    def __init__(self):

        vsync = True
        if settings.getboolean('all', 'performance_test'):
            vsync = False

        self.win = Window(width=1024, height=768, vsync=vsync)
        self.win.set_exclusive_mouse()

        self.music = Music()
        self.music.play()

        self.win.push_handlers(self)

        self.arena = Arena(self, self.win.width, self.win.height)
        GameItem.arena = self.arena
        self.game = Game(self.arena)

        self.render = Render(self, self.win)
        self.render.init(self.win)
        self.win.on_draw = self.render.draw

        self.game.init(self.render.images)

        if settings.getboolean('all', 'performance_test'):
            self.arena.spawn_enemy(
                number=256,
                delay=0.01,
                player=self.player)

        clock.schedule(self.arena.update)


    def on_key_press(self, symbol, _):
        if symbol == key.M:
            self.music.toggle()
        elif symbol == key.ESCAPE:
            self.win.close()

