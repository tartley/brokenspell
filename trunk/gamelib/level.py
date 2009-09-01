import math

from itertools import islice

from pyglet.text import Label

from feather import Feather
from gameent import GameEnt


class Level(object):

    width = None
    height = None

    def __init__(self, width, height):
        Level.width = width
        Level.height = height
        self.age = 0.0
        self.ents = []
        self.score = 0
        GameEnt.level = self


    def add(self, ent):
        self.ents.append(ent)


    def collision(self, ent1, ent2):
        if math.sqrt(((ent1.center_x + ent1.x) - (ent2.center_x + ent2.x)) ** 2 + 
                ((ent1.center_y + ent1.y) - (ent2.center_y + ent2.y)) ** 2) < max(ent1.width, ent2.width) * 0.8:
            return True


    def draw(self):
        score = 'Score: %d' % self.score
        score_label = Label(score,
                font_size=36, x=Level.width, y=Level.height,
                anchor_x='right', anchor_y='top')
        score_label.draw()

        for ent in self.ents:
            ent.draw()


    def wraparound(self, ent):
        if ent.x < ent.width:
            ent.x += Level.width + ent.width
        if ent.x > Level.width:
            ent.x -= Level.width + ent.width


    def detect_collisions(self):
        for i, ent1 in enumerate(self.ents):
            for ent2 in islice(self.ents, i+1, None):
                if self.collision(ent1, ent2):
                    ent1.collided_with(ent2)
                    ent2.collided_with(ent1)


    def remove_dead(self):
        for ent in self.ents[:]:
            if ent.remove_from_game:
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


