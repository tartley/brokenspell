
from player import Player


class Level(object):

    def __init__(self):
        self.age = 0.0
        self.player = Player()


    def draw(self):
        if self.player:
            self.player.draw()


    def update(self, dt):
        self.age += dt

