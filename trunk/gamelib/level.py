import math

from feather import Feather

class Level(object):

    def __init__(self, width, height):
        self.age = 0.0
        self.ents = []
        self.width = width
        self.height = height

    
    def add(self, ent):
        self.ents.append(ent)


    def collision(self, ent1, ent2):
        if math.sqrt(((ent1.center_x + ent1.x) - (ent2.center_x + ent2.x)) ** 2 + 
                ((ent1.center_y + ent1.y) - (ent2.center_y + ent2.y)) ** 2) < max(ent1.width, ent2.width) * 0.8:
            return True


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

        for ent in self.ents[:]:

            for collider in self.ents:
                if collider == ent:
                    continue
                if self.collision(ent, collider):
                    ent.collided_with(collider)

            if ent.dead:
                self.ents.remove(ent)
                self.ents.append(Feather(ent.x, ent.y))
                continue

            ent.update()
            self.wraparound(ent)

