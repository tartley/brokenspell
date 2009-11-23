
from random import randint, uniform

from pyglet import clock
from pyglet.window import key

from bird import Bird
from config import settings
from enemy import Enemy
from gameitem import GameItem
from ground import Ground
from hudmessage import HudMessage
from hudpoints import HudPoints
from hudscore import HudScore
from hudtitle import HudTitle
from hudinstructions import HudInstructions
from feather import Feather
from player import Player
from sky import Sky
from sounds import play



class GameControls(key.KeyStateHandler):

    def __init__(self, win, game, arena):
        self.win = win
        self.game = game
        self.arena = arena


    def update(self):
        if self[key.F1]:
            hudpoints = HudPoints(
                randint(0, self.win.width),
                randint(0, self.win.height),
                randint(0, 8))
            self.arena.add(hudpoints)

        if self[key.F2]:
            self.game.spawn_enemy(dx=5)

        if self[key.F3]:
            for item in self.arena.items:
                if isinstance(item, Bird):
                    item.feathers += 1
                    item.lose_feather(item.x + 30, item.y + 30)



class Game(object):

    def __init__(self, win):
        self.win = win
        self.score = 0
        self.wave = 0
        self.num_enemies = 0
        self.gamecontrols = None
        self.arena = None


    def init(self, arena):
        self.arena = GameItem.arena = arena

        arena.item_added += self.on_add_item
        arena.item_removed += self.on_remove_item

        sky = Sky(self.win.width, self.win.height)
        arena.add(sky)

        ground = Ground()
        arena.add(ground)

        hudtitle = HudTitle(self, self.win.width, self.win.height)
        arena.add(hudtitle)

        self.gamecontrols = GameControls(self.win, self, arena)
        self.win.push_handlers(self.gamecontrols)

        clock.schedule(self.update)


    def start(self):
        self.get_ready()

        self.arena.add(
            HudInstructions(self, self.win.width, self.win.height))

        hudscore = HudScore(self, self.win.width, self.win.height)
        clock.schedule_once(lambda _: self.arena.add(hudscore), 1)

        clock.schedule_once(lambda _: self.spawn_wave(), 3)


    def get_ready(self):
        self.arena.add(HudMessage('Get Ready!', 36))
        clock.schedule_once(lambda _: self.spawn_player(), 1)


    def spawn_player(self):
        player = Player(
            self.win.width / 2, self.win.height + Player.height / 2,
            self)
        player.remove_from_game = False
        player.is_alive = True
        self.arena.add(player)


    def spawn_wave(self, number=None):
        self.wave += 1
        if number is None:
            number = self.wave * self.wave

        self.arena.add(HudMessage('Wave %d' % (self.wave,), 36))

        for n in xrange(number):
            clock.schedule_once(lambda _: self.spawn_enemy(), n)


    def spawn_enemy(self, x=None, y=None, dx=None, dy=None):
        if x is None:
            x = uniform(0, self.win.width)
        if y is None:
            y = self.win.height + 32
        if dx is None:
            dx = uniform(-20, 20)
        if dy is None:
            dy = 0
        self.arena.add(Enemy(x, y, dx=dx, dy=0))


    def update(self, _):
        self.arena.update()
        self.gamecontrols.update()


    def on_add_item(self, _, item):
        if isinstance(item, Enemy):
            self.num_enemies += 1


    def on_remove_item(self, _, item):
        if isinstance(item, Enemy):
            self.num_enemies -= 1
            if self.num_enemies == 0:
                self.spawn_wave()

        if isinstance(item, Player):
            clock.schedule_once(lambda _: self.get_ready(), 2)

