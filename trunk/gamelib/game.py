
from random import uniform

from pyglet import clock

from arena import Arena
from config import settings
from enemy import Enemy
from gameitem import GameItem
from ground import Ground
from hudmessage import HudMessage
from hudscore import HudScore
from hudtitle import HudTitle
from hudinstructions import HudInstructions
from feather import Feather
from player import Player
from sky import Sky
from sounds import play


class Game(object):

    def __init__(self, win):
        self.width = win.width
        self.height = win.height
        self.score = 0
        self.num_enemies = 0
        self.wave = 0

        self.arena = Arena(win, self)
        GameItem.arena = self.arena


    def set_worlditem_images_and_sizes(self, images):
        for klass in [Ground, Player, Enemy, Feather]:
            klass.images = images[klass.__name__]
            klass.width = klass.images[0].width
            klass.height = klass.images[0].height


    def init(self, images):
        self.set_worlditem_images_and_sizes(images)

        self.arena.item_added += self.on_add_item
        self.arena.item_removed += self.on_remove_item

        sky = Sky(self.width, self.height)
        self.arena.add(sky)

        ground = Ground()
        self.arena.add(ground)

        hudtitle = HudTitle(self, self.width, self.height)
        self.arena.add(hudtitle)

        if settings.getboolean('all', 'performance_test'):
            for n in xrange(256):
                clock.schedule_once(lambda _: self.spawn_enemy(), 0.01 * n)

        clock.schedule(self.arena.update)


    def start(self):
        self.get_ready()

        hudscore = HudScore(self, self.width, self.height)
        self.arena.add(hudscore)

        hudinstructions = HudInstructions(
            self, self.width, self.height)
        self.arena.add(hudinstructions)

        clock.schedule_once(lambda _: self.spawn_wave(), 3)


    def get_ready(self):
        self.arena.add(HudMessage('Get Ready!', self))
        clock.schedule_once(lambda _: self.spawn_player(), 2)


    def spawn_player(self):
        player = Player(self.width / 2, self.height, self)
        player.remove_from_game = False
        player.is_alive = True
        self.arena.add(player)


    def spawn_wave(self, number=None):
        self.wave += 1
        if number is None:
            number = self.wave

        self.arena.add(HudMessage('Wave %d' % (self.wave), self))

        for n in xrange(number):
            clock.schedule_once(lambda _: self.spawn_enemy(), n)


    def spawn_enemy(self):
        x = uniform(0, self.width)
        y = self.height + 32
        dx = uniform(-20, 20)
        self.arena.add(Enemy(x, y, dx=dx, dy=0))


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

