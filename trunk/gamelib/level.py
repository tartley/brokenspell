

class Level(object):

    def __init__(self, player):
        self.age = 0.0
        self.gameents = [player]
        self.width = 1024


    def draw(self):
        for ent in self.gameents:
            ent.draw()


    def wraparound(self, ent):
        if ent.x < -70:
            ent.x += self.width + 70
        if ent.x > self.width:
            ent.x -= self.width + 70


    def update(self, dt):
        self.age += dt
        for ent in self.gameents:
            ent.update(dt)
            self.wraparound(ent)


