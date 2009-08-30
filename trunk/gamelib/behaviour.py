
from random import randint 

from bird import Action


class Hover(object):

    def __init__(self, ent):
        self.ent = ent

    def __call__(self):
        if randint(0, 30) == 1:
            return set([Action.FLAP])
        return set()

