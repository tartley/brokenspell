
from sky import Sky


class Game(object):

    def __init__(self, arena):
        self.arena = arena
        self.score = 0

    def startup(self):
        sky = Sky(self.arena.width, self.arena.height)
        self.arena.add(sky)

