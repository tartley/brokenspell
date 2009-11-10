
from hudscore import HudScore
from sky import Sky
from ground import Ground


class Game(object):

    def __init__(self, arena):
        self.arena = arena
        self.score = 0

    def startup(self, images):
        sky = Sky(self.arena.width, self.arena.height)
        self.arena.add(sky)

        ground = Ground()
        self.arena.add(ground)

        hudscore = HudScore(self, self.arena.width, self.arena.height)
        self.arena.add(hudscore)

