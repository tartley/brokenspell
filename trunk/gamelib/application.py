
from pyglet import app, clock
from pyglet.window import key, Window

from arena import Arena
from config import settings
from game import Game
from gameitem import GameItem
from music import Music
from player import Player
from render import Render
from sounds import play


MESSAGE_WAVE1 = [
    '',
    'Attack from above',
    'Avoid enemies above you',
    'Lowest bird loses feathers',
]


class KeyHandler(object):
    app = None


class ToggleMusic(KeyHandler):

    def __init__(self, music):
        self.music = music

    def on_key_press(self, symbol, _):
        if symbol == key.M:
            self.music.toggle()


class Application(object):

    def __init__(self):

        vsync = True
        if settings.getboolean('all', 'performance_test'):
            vsync = False

        self.win = Window(width=1024, height=768, vsync=vsync)
        self.win.set_exclusive_mouse()

        self.music = Music()
        self.music.play()

        self.keyhandler = key.KeyStateHandler()
        self.win.push_handlers(self.keyhandler)
        self.win.push_handlers(ToggleMusic(self.music))

        self.player = None

        self.arena = Arena(self, self.win.width, self.win.height)
        GameItem.arena = self.arena
        self.game = Game(self.arena, self.player)

        self.render = Render(self, self.win)
        self.render.init(self.win)
        self.win.on_draw = self.render.draw

        self.game.init(self.render.images)

        self.resurrecting = False

        KeyHandler.app = self

        if settings.getboolean('all', 'performance_test'):
            self.arena.spawn_enemy(
                number=256,
                delay=0.01,
                player=self.player)

        clock.schedule(self.update)


    def get_ready(self):
        self.player.reincarnate(self.arena.width / 2, self.arena.height)
        clock.schedule_once(lambda _: self.spawn_player(), 1)


    def spawn_player(self):
        if not self.player:
            self.player = Player(
                self.keyhandler,
                self.arena.width / 2, self.arena.height,
                self.game)
        self.player.remove_from_game = False
        self.player.is_alive = True
        self.arena.add(self.player)
        self.resurrecting = False
        return self.player


    def update(self, dt):
        self.arena.update(dt)

        if self.player and not self.player.is_alive and not self.resurrecting:
            self.resurrecting = True
            play('ohno')
            clock.schedule_once(lambda _: self.get_ready(), 2)


    def run(self):
        app.run()

