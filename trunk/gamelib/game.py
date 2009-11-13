
from pyglet import clock

from enemy import Enemy
from ground import Ground
from hudmessage import HudMessage
from hudscore import HudScore
from hudtitle import HudPressAnyKey
from hudinstructions import HudInstructions
from player import Player
from sky import Sky
from sounds import play


class Game(object):

    def __init__(self, arena):
        self.arena = arena
        self.score = 0
        self.player = None

        self.num_enemies = 0

        arena.item_added += self.on_add_item
        arena.item_removed += self.on_remove_item


    def init(self, images):
        sky = Sky(self.arena.width, self.arena.height)
        self.arena.add(sky)

        ground = Ground()
        self.arena.add(ground)

        hudtitle = HudPressAnyKey(self, self.arena.width, self.arena.height)
        self.arena.add(hudtitle)


    def start(self):
        self.get_ready()

        hudscore = HudScore(self, self.arena.width, self.arena.height)
        self.arena.add(hudscore)

        hudinstructions = HudInstructions(
            self, self.arena.width, self.arena.height)
        self.arena.add(hudinstructions)

        clock.schedule_once(lambda _: self.spawn_wave(), 3)


    def get_ready(self):
        self.arena.add(
            HudMessage('Get Ready!',
                self, self.arena.width, self.arena.height))
        clock.schedule_once(lambda _: self.spawn_player(), 2)


    def spawn_player(self):
        self.player = Player(self.arena.width / 2, self.arena.height, self)
        self.player.remove_from_game = False
        self.player.is_alive = True
        self.arena.add(self.player)


    def spawn_wave(self):
        self.arena.add(
            HudMessage('Here they come...',
                self, self.arena.width, self.arena.height))
        clock.schedule_once(
            lambda _: self.arena.spawn_enemy(4, 1.7, self.player), 2)


    def on_add_item(self, _, item):
        if isinstance(item, Enemy):
            self.num_enemies += 1


    def on_remove_item(self, _, item):
        if isinstance(item, Enemy):
            self.num_enemies -= 1
            if self.num_enemies == 0:
                self.spawn_wave()

        if isinstance(item, Player):
            self.player = None
            self.arena.add(
                HudMessage('Oh no!',
                    self, self.arena.width, self.arena.height))
            play('ohno')
            clock.schedule_once(lambda _: self.get_ready(), 2)

