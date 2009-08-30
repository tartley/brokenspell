
from random import uniform


class Think(object):

    def update(self):
        pass


class Hover(object):

    def __init__(self, ent):
        self.ent = ent

    def update(self):
        if uniform(0, 5) == 0:
            ent.try_flap()

