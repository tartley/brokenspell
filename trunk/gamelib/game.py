
from sky import Sky


class Game(object):

    def __init__(self, world):
        self.world = world
        self.score = 0

    def startup(self):
        sky = Sky(self.world.width, self.world.height)
        self.world.add(sky)

