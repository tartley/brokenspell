
from pyglet import clock


DELAY = 3


class Multiplier(object):

    def __init__(self):
        self.value = 1


    def schedule_decrement(self):
        clock.unschedule(self._decrement)
        clock.schedule_once(self._decrement, DELAY)


    def increment(self):
        self.value += 1
        self.schedule_decrement()


    def _decrement(self, _):
        if self.value > 1:
            self.value -= 1
            if self.value > 1:
                self.schedule_decrement()

