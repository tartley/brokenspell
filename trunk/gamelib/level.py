

class Level(object):

    def __init__(self, player):
        self.age = 0.0
        self.player = player


    def draw(self):
        self.player.draw()


    def update(self, dt):
        self.age += dt
        self.player.update(dt)

