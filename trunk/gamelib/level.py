import math

from itertools import islice

from pyglet.text import Label

from feather import Feather
from gameent import GameEnt


class Level(object):

    def __init__(self, width, height):
        self.age = 0.0
        self.ents = []
        self.width = width
        self.height = height
        self.score = 0
        self.player = None
        GameEnt.level = self


    def add(self, ent):
        self.ents.append(ent)


    def add_player(self, ent):
        self.player = ent
        self.add(ent)


    def collision(self, ent1, ent2):
        if math.sqrt(((ent1.center_x + ent1.x) - (ent2.center_x + ent2.x)) ** 2 + 
                ((ent1.center_y + ent1.y) - (ent2.center_y + ent2.y)) ** 2) < max(ent1.width, ent2.width) * 0.8:
            return True


    def draw(self):
        score = 'Score: %d' % self.score
        score_label = Label(score,
                font_size=36, x=self.width, y=self.height,
                anchor_x='right', anchor_y='top')
        score_label.draw()

        for ent in self.ents:
            ent.draw()


    def wraparound(self, ent):
        if ent.x < ent.width:
            ent.x += self.width + ent.width
        if ent.x > self.width:
            ent.x -= self.width + ent.width


    def reset_player(self):
        self.player.x = self.width / 2
        self.player.y = self.height
        self.player.is_alive = True
        self.score = 0


    def detect_collisions(self):
        print '.',
        for i, ent1 in enumerate(self.ents):
            for ent2 in islice(self.ents, i+1, None):
                if self.collision(ent1, ent2):
                    print 'C', type(ent1).__name__, type(ent2).__name__,
                    ent1.collided_with(ent2)
                    ent2.collided_with(ent1)


    def remove_dead(self):
        for ent in self.ents[:]:
            if ent.is_gone:
                self.ents.remove(ent)


    def update_ents(self):
        for ent in self.ents:
            ent.update()
            self.wraparound(ent)


    def is_player_dead(self):
        return not self.player.is_alive and self.player.y <= 0


    def update(self, dt):
        self.age += dt
        self.detect_collisions()
        self.remove_dead()
        self.update_ents()
        return self.is_player_dead()


