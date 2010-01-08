
from random import randint

from pyglet import clock


FLAP_RATE = 20


class Action(object):
    FLAP = 0
    LEFT = 1
    RIGHT = 2


class State(object):
    def __init__(self, item):
        self.item = item

    def get_actions(self):
        return set()


class Plummet(State):
    pass


class Hover(State):

    def __init__(self, *args):
        State.__init__(self, *args)
        self.choose_altitude(None)


    def choose_altitude(self, _):
        if not self.item.is_alive:
            return
        self.desired_y = randint(100, self.item.game.height - 100)
        clock.schedule_once(self.choose_altitude, randint(3, 20))


    def get_actions(self):
        if (
            self.item.last_flap < FLAP_RATE / 2.0
            or
            (
                self.item.y < self.desired_y and
                self.item.last_flap > FLAP_RATE
            )
        ):
            return set([Action.FLAP])
        return set()



class Cruise(Hover):

    def __init__(self, item, fast):
        Hover.__init__(self, item)
        self.fast = fast
        if self.item.dx < 0:
            self.direction = Action.LEFT
        else:
            self.direction = Action.RIGHT

    def get_actions(self):
        actions = Hover.get_actions(self)
        if self.fast:
            actions.add(self.direction)
        else:
            if not actions and self.item.last_flap > FLAP_RATE / 2:
                actions = set([self.direction])
        return actions


class Thinker(object):

    def __init__(self, item, fast, behaviour=None):
        self.item = item
        if behaviour is None:
            behaviour = Cruise(item, fast)
        self.state = behaviour

    def __call__(self):
        return self.state.get_actions()


    def face_away(self, other):
        if self.item.x < other.x:
            self.state.direction = Action.LEFT
        else:
            self.state.direction = Action.RIGHT

