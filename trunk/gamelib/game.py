
from pyglet import clock

from enemy import Enemy
from ground import Ground
from hudscore import HudScore
from hudtitle import HudPressAnyKey
from hudinstructions import HudInstructions
from player import Player
from sky import Sky


class Game(object):

    def __init__(self, arena):
        self.arena = arena
        self.score = 0
        self.player = None

        self.num_enemies = 0

        arena.item_added += self.on_add_item
        arena.item_removed += self.on_remove_item

        self.resurrecting = False # TODO remove this


    def init(self, images):
        sky = Sky(self.arena.width, self.arena.height)
        self.arena.add(sky)

        ground = Ground()
        self.arena.add(ground)

        hudtitle = HudPressAnyKey(self, self.arena.width, self.arena.height)
        self.arena.add(hudtitle)


    def start(self):
        self.player = Player(self.arena.width / 2, self.arena.height, self)
        self.spawn_player(self.player)

        hudinstructions = HudInstructions(
            self, self.arena.width, self.arena.height)
        self.arena.add(hudinstructions)

        hudscore = HudScore(self, self.arena.width, self.arena.height)
        self.arena.add(hudscore)

        self.spawn_wave()


    def spawn_player(self, player):
        self.player.remove_from_game = False
        self.player.is_alive = True
        self.arena.add(self.player)
        self.resurrecting = False


    def spawn_wave(self):
        clock.schedule_once(
            lambda _: self.arena.spawn_enemy(4, 1.7, self.player),
            2)


    def on_add_item(self, _, item):
        if isinstance(item, Enemy):
            self.num_enemies += 1


    def on_remove_item(self, _, item):
        if isinstance(item, Enemy):
            self.num_enemies -= 1
            if self.num_enemies == 0:
                self.spawn_wave()


