
from random import randint 

from bird import Action


class State(object):
    def __init__(self, ent):
        self.ent = ent
        self.new_state = None

    def get_actions(self):
        return set()


class Hover(State):

    def __init__(self, *args):
        State.__init__(self, *args)
        self.desired_y = randint(0, self.ent.y)

    def get_actions(self):
        if self.ent.y < self.desired_y and self.ent.last_flap > 1:
            return set([Action.FLAP])
        return set()


class Cruise(State):
    pass


class Thinker(object):

    def __init__(self, ent):
        self.state = Hover(ent)

    def __call__(self):
        actions = self.state.get_actions()
        # if self.state.new_state:
        #     self.state = new_state
        return actions

