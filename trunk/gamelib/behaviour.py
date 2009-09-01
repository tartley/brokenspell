
from random import randint 


class Action(object):
    FLAP = 0
    LEFT = 1
    RIGHT = 2


class State(object):
    def __init__(self, ent):
        self.ent = ent

    def get_actions(self):
        return set()


class Plummet(State):
    pass


class Hover(State):

    def __init__(self, *args):
        State.__init__(self, *args)
        self.desired_y = randint(0, self.ent.y)

    def get_actions(self):
        if self.ent.y < self.desired_y and self.ent.last_flap > 10:
            return set([Action.FLAP])
        return set()


class Cruise(Hover):

    def __init__(self, ent):
        Hover.__init__(self, ent)
        if self.ent.dx < 0:
            self.direction = Action.LEFT
        else:
            self.direction = Action.RIGHT

    def get_actions(self):
        actions = Hover.get_actions(self)
        if self.ent.last_flap % 2 == 1:
            actions = set([self.direction])
        return actions


class Thinker(object):

    def __init__(self, ent):
        self.state = Cruise(ent)

    def __call__(self):
        return self.state.get_actions()

