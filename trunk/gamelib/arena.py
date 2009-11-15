
import math

from itertools import islice

from pyglet import clock, image

from config import settings
from enemy import Enemy
from event import Event
from feather import Feather
from worlditem import WorldItem


def is_touching(item1, item2):
    distance = math.hypot(
        (item1.center_x + item1.x) - (item2.center_x + item2.x),
        (item1.center_y + item1.y) - (item2.center_y + item2.y)
    )
    if distance < max(item1.width, item2.width) * 0.8:
        return True


class ItemAdded(Event): pass
class ItemRemoved(Event): pass


class Arena(object):

    def __init__(self, win, game):
        self.win = win
        self.game = game

        self.items = []

        self.item_added = ItemAdded()
        self.item_removed = ItemRemoved()


    def add(self, item):
        self.items.append(item)

        if hasattr(item, 'on_key_press'):
            self.win.push_handlers(item)

        self.item_added(self, item)


    def remove(self, item):
        self.items.remove(item)

        if hasattr(item, 'on_key_press'):
            self.win.remove_handlers(item)

        self.item_removed(self, item)


    def detect_collisions(self):
        if settings.getboolean('all', 'performance_test'):
            return

        for i, item1 in enumerate(self.items):
            for item2 in islice(self.items, i+1, None):
                if (
                    isinstance(item1, WorldItem) and
                    isinstance(item2, WorldItem) and
                    is_touching(item1, item2)
                ):
                    item1.collided_with(item2)
                    item2.collided_with(item1)


    def remove_dead(self):
        for item in self.items[:]:
            if item.remove_from_game:
                self.remove(item)


    def update(self, dt):
        self.detect_collisions()
        for item in self.items:
            if hasattr(item, 'update'):
                item.update()
            if hasattr(item, 'wraparound'):
                item.wraparound(self.win.width)
        self.remove_dead()

