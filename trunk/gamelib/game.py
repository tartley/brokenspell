
from pyglet import clock

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

        self.resurrecting = False # TODO remove this


    def init(self, images):
        sky = Sky(self.arena.width, self.arena.height)
        self.arena.add(sky)

        ground = Ground()
        self.arena.add(ground)

        # TODO: this should only be created when game starts
        hudscore = HudScore(self, self.arena.width, self.arena.height)
        self.arena.add(hudscore)

        hudtitle = HudPressAnyKey(self, self.arena.width, self.arena.height)
        self.arena.add(hudtitle)


    @property
    def age(self):
        return self.age - self.born


    def start(self):
        self.player = Player(
            self.arena.width / 2, self.arena.height,
            self)
        self.spawn_player(self.player)

        hudinstructions = HudInstructions(
            self, self.arena.width, self.arena.height)
        self.arena.add(hudinstructions)

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
