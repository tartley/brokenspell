

class Level(object):

    def __init__(self, width, height):
        self.age = 0.0
        self.ents = []
        self.width = width
        self.height = height

    
    def add(self, ent):
        self.ents.append(ent)


    def draw(self):
        for ent in self.ents:
            ent.draw()


    def wraparound(self, ent):
        if ent.x < -70:
            ent.x += self.width + 70
        if ent.x > self.width:
            ent.x -= self.width + 70


    def update(self, dt):
        self.age += dt
        for ent in self.ents:
            ent.update()
            self.wraparound(ent)


