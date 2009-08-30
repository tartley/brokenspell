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
                    self.collided_with(ent, collider)

            if hasattr(ent, 'feathers') and ent.feathers == 0:
                self.ents.remove(ent)
                continue

            ent.update()
            self.wraparound(ent)


    def collided_with(self, ent1, ent2):
        if ent2.canDie and hasattr(ent1, 'is_player'):
            if ent2.y < ent1.y:
                ent2.feathers -= 1
                self.ents.append(Feather(ent2.x, ent2.y, ent2.dx, ent2.dy))


            ent1.dy = 10 - ent1.dy
            x_direction = math.copysign(1, ent1.x - ent2.x) 
            ent1.dx =  x_direction * 10 - x_direction * ent2.dx
