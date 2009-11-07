
from pyglet import app, clock
from pyglet.window import key, Window

from config import settings
from game import Game
from gameent import GameEnt
from instructions import Instructions
from world import World
from player import Player
from render import Render
from sounds import play
from music import Music


MESSAGE_TITLE = 'Sinister Ducks'
MESSAGE_ANYKEY = ['Press any key...', '']

MESSAGE_CONTROLS = [
    'Z to flap wings',
    'Left and Right to steer',
]

MESSAGE_WAVE1 = [
    '',
    'Attack from above',
    'Avoid enemies above you',
    'Lowest bird loses feathers',
]


class KeyHandler(object):
    app = None

class AnyKeyStartsGame(KeyHandler):
    def on_key_press(self, _, __):
        self.app.user_message.clear()
        self.app.instructions.clear()
        self.app.spawn_player()

        def start_instructions(_):
            self.app.show_instructions(None)
            self.app.win.push_handlers(UseControlsSkipsInstruction())

        self.app.win.pop_handlers()
        clock.schedule_once(start_instructions, 2)


class UseControlsSkipsInstruction(KeyHandler):
    def __init__(self):
        self.pressed = set()

    def on_key_press(self, symbol, _):
        self.pressed.add(symbol)
        all_controls_used = (
            (key.LEFT in self.pressed or key.RIGHT in self.pressed) and
            key.Z in self.pressed
        )

        delay = 1
        if settings.getboolean('all', 'show_intro'):
            delay = 18.25

        if all_controls_used:
            self.app.win.pop_handlers()
            self.app.user_message.set_messages(MESSAGE_WAVE1)

            clock.schedule_once(
               lambda _: self.app.world.spawn_enemy(
                   number=8,
                   delay=1.7,
                   player=self.app.player),
               max(delay - self.app.world.age, 1))


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
        self.player = None

        self.music = Music()
        self.music.play()

        self.keyhandler = key.KeyStateHandler()
        self.win.push_handlers(self.keyhandler)
        self.win.push_handlers(ToggleMusic(self.music))

        self.world = World(self, self.win.width, self.win.height)
        GameEnt.world = self.world

        self.render = Render(self)
        self.render.init()

        self.resurrecting = False

        self.user_message = Instructions(
            MESSAGE_TITLE, self.win.width/2, self.win.height/2 + 30,
            'center', 'center',
            delay=None)
        self.instructions = Instructions(
            MESSAGE_ANYKEY, self.win.width/2, self.win.height/2 - 20,
            'center', 'center',
            delay=0.5, repeat=True, size=20)

        self.game = Game()

        KeyHandler.app = self

        if settings.getboolean('all', 'performance_test'):
            self.world.spawn_enemy(
                number=256,
                delay=0.01,
                player=self.player)

        self.win.push_handlers(AnyKeyStartsGame())
        clock.schedule(self.update)


    def get_ready(self):
        self.player.reincarnate(self.world.width / 2, self.world.height)
        self.user_message.set_messages('Get ready...')
        clock.schedule_once(lambda _: self.spawn_player(), 1)


    def show_instructions(self, _):
        self.user_message.set_messages(MESSAGE_CONTROLS, repeat=True)


    def spawn_player(self):
        if not self.player:
            self.player = Player(
                self.keyhandler,
                self.world.width / 2, self.world.height,
                self.game)
        self.player.remove_from_game = False
        self.player.is_alive = True
        self.world.add(self.player)
        self.resurrecting = False


    def update(self, dt):
        self.world.update(dt)

        if self.player and not self.player.is_alive and not self.resurrecting:
            self.resurrecting = True
            self.user_message.set_messages('Oh no!')
            play('ohno')
            clock.schedule_once(lambda _: self.get_ready(), 2)


    def next_wave(self):
        self.wave += 1
        self.user_message.set_messages('Wave %d' % (self.wave,))
        clock.schedule_once(
            lambda _: self.world.spawn_enemy(self.wave, 1.7, self.player),
            2)


def main():
    application = Application()
    app.run()

