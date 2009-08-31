import math

from pyglet.text import Label

from feather import Feather


class Level(object):

    def __init__(self, width, height):
        self.age = 0.0
        self.ents = []
        self.width = width
        self.height = height
        self.score = 0

    
    def add(self, ent):
        self.ents.append(ent)


    def collision(self, ent1, ent2):
        if math.sqrt(((ent1.center_x + ent1.x) - (ent2.center_x + ent2.x)) ** 2 + 
                ((ent1.center_y + ent1.y) - (ent2.center_y + ent2.y)) ** 2) < max(ent1.width, ent2.width) * 0.8:
            return True


    def draw(self):
        score = 'Score: %d' % self.score
        score_label = Label(score,
                font_size=36, x=1024, y=768,
                anchor_x='right', anchor_y='top')
        score_label.draw()

        for ent in self.ents:
            ent.draw()
            

    def wraparound(self, ent):
        if ent.x < -70:
            ent.x += self.width + 70
        if ent.x > self.width:
            ent.x -= self.width + 70


    def reset(self):
        self.score = 0
        self.ents = [e for e in self.ents if hasattr(e, 'is_player')]


    def detect_collisions(self):
        for ent in self.ents:
            for collider in self.ents:
                if collider == ent:
                    continue
                if self.collision(ent, collider):
                    self.collided_with(ent, collider)
    

    def remove_dead(self):
        for ent in self.ents[:]:
            if ent.is_gone:
                self.ents.remove(ent)


    def update_ents(self):
        for ent in self.ents:
            ent.update()
            self.wraparound(ent)    


    def update(self, dt):
        self.age += dt
        self.detect_collisions()
        self.remove_dead()
        self.update_ents()


    def collided_with(self, ent1, ent2):
        if hasattr(ent2, 'is_enemy') and hasattr(ent1, 'is_player'):
            if ent2.y < ent1.y:
                ent2.feathers -= 1
                self.ents.append(Feather(ent2.x, ent2.y, ent2.dx, ent2.dy))
                ent1.dy = 10 - ent1.dy
                x_direction = math.copysign(1, ent1.x - ent2.x) 
                ent1.dx =  x_direction * 10 - x_direction * ent2.dx
            else:
                self.reset()

        if hasattr(ent2, 'is_feather') and hasattr(ent1, 'is_player'):
            self.ents.remove(ent2)
            self.score += 10

