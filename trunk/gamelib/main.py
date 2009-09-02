
from os.path import join

from pyglet import app, clock
from pyglet.event import EVENT_HANDLED
from pyglet.gl import (
    glBlendFunc, glClearColor, glClear, glEnable, glLoadIdentity, glMatrixMode,
    gluOrtho2D, 
    GL_BLEND, GL_COLOR_BUFFER_BIT, GL_ONE_MINUS_SRC_ALPHA, GL_PROJECTION,
    GL_QUADS, GL_SRC_ALPHA,
)
from pyglet.graphics import draw
from pyglet.window import key, Window
from pyglet.media import load

from enemy import Enemy
from instructions import Instructions
from player import Player
from level import Level


clockDisplay = clock.ClockDisplay()


MESSAGE_TITLE = 'Sinister Ducks'
MESSAGE_ANYKEY = ['', 'Press any key...']

MESSAGE_CONTROLS = [
    'Z to flap wings',
    'Left and Right to steer',
]

MESSAGE_INSTRUCTIONS = [
    '',
    'Collide with enemies to joust',
    'Lowest bird sheds feathers',
    'Collect feathers FTW!',
]


class KeyHandler(object):
    app = None

class AnyKeyStartsGame(KeyHandler):
    def on_key_press(self, _, __):
        self.app.user_message.clear()
        self.app.instructions.clear()
        self.app.spawn_player()
        clock.schedule_once(self.app.show_instructions, 2)
        self.app.win.pop_handlers()
        self.app.win.push_handlers(UseControlsSkipsInstruction())

class UseControlsSkipsInstruction(KeyHandler):
    def __init__(self):
        self.pressed = set()

    def on_key_press(self, symbol, _):
        self.pressed.add(symbol)
        all_controls_used = (
            (key.LEFT in self.pressed or key.RIGHT in self.pressed) and
            key.Z in self.pressed
        )
        if all_controls_used:
            self.app.user_message.clear()
            self.app.win.pop_handlers()
            self.app.user_message.set_messages(
                MESSAGE_INSTRUCTIONS, repeat=False)
            clock.schedule_once(
               lambda _: self.app.level.spawn_enemy(8, self.app.player),
               18.25 - self.app.level.age)


class Application(object):

    def __init__(self):
        self.win = Window(width=1024, height=768)
        self.win.set_exclusive_mouse()
        self.win.on_draw = self.draw
        self.player = None
        music = load(join('data', 'music2.mp3'))
        clock.schedule_once(lambda _: music.play(), 1)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.keyhandler = key.KeyStateHandler()
        self.win.push_handlers(self.keyhandler)

        self.level = Level(self.win.width, self.win.height)
        self.resurrecting = False

        self.user_message = Instructions(
            MESSAGE_TITLE, self.win.width/2, self.win.height/2 + 30,
            'center', 'center',
            delay=None)
        self.instructions = Instructions(
            MESSAGE_ANYKEY, self.win.width/2, self.win.height/2 - 20,
            'center', 'center',
            delay=1, size=20)

        KeyHandler.app = self
        self.win.push_handlers(AnyKeyStartsGame())
        clock.schedule(self.update)


    def get_ready(self):
        self.player.reincarnate(self.level.width / 2, self.level.height)
        self.user_message.set_messages('Get ready...')
        clock.schedule_once(lambda _: self.spawn_player(), 1)



    def show_instructions(self, _):
        self.user_message.set_messages(MESSAGE_CONTROLS)


    def spawn_player(self):
        if not self.player:
            self.player = Player(
                self.keyhandler,
                self.level.width / 2, self.level.height)
        self.player.remove_from_game = False
        self.player.is_alive = True
        self.level.add(self.player)
        self.resurrecting = False


    def update(self, dt):
        self.level.update(dt)
        if self.player and not self.player.is_alive and not self.resurrecting:
            self.resurrecting = True
            # self.user_message.set_message('Oh no!')
            clock.schedule_once(lambda _: self.get_ready(), 2)


    def draw(self):
        self.gradient_clear()
        self.level.draw()
        self.user_message.draw()
        self.instructions.draw()
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


def main():
    application = Application()
    app.run()

