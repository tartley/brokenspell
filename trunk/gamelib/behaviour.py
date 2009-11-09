
from random import randint

from pyglet import clock


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

    scheduled = {}

    def __init__(self, *args):
        State.__init__(self, *args)
        self.choose_altitude(None)


    def choose_altitude(self, _):
        if not self.item.is_alive:
            return

        self.desired_y = randint(100, self.item.arena.height - 100)
        clock.schedule_once(self.choose_altitude, randint(3, 20))


    def get_actions(self):
        foe_is_below = (
            self.item.foe and
            self.item.foe.y < self.item.y and
            abs(self.item.foe.x - self.item.x) < self.item.width
        )
        if foe_is_below:
            return set()
        if self.item.foe:
            foe_x = self.item.foe.x
            self.item.foe = None
            if foe_x < self.item.x:
                self.direction = Action.RIGHT
                return set()
            else:
                self.direction = Action.LEFT
                return set()

        flap_rate = 15
        if self.item.y < self.desired_y and self.item.last_flap > flap_rate:
            return set([Action.FLAP])
        return set()


class Cruise(Hover):

    def __init__(self, item):
        Hover.__init__(self, item)
        if self.item.dx < 0:
            self.direction = Action.LEFT
        else:
            self.direction = Action.RIGHT

    def get_actions(self):
        actions = Hover.get_actions(self)
        if not actions and self.item.last_flap % 2 == 1:
            actions = set([self.direction])
        return actions


class Thinker(object):

    def __init__(self, item):
        self.state = Cruise(item)

    def __call__(self):
        return self.state.get_actions()

