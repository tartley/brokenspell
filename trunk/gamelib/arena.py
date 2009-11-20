
import math

from itertools import islice

from pyglet import clock, image

from config import settings
from enemy import Enemy
from event import Event
from feather import Feather
from worlditem import WorldItem


def is_touching(item1, item2):
    if not isinstance(item1, WorldItem) or not isinstance(item2, WorldItem):
        return False
    border = 6
    w1 = item1.width / 2 - border
    w2 = item2.width / 2 - border
    h1 = item1.height / 2 - border
    h2 = item2.height / 2 - border
    return (
        (item1.x - w1) < (item2.x + w2) and
        (item2.x - w2) < (item1.x + w1) and
        (item1.y - h1) < (item2.y + h2) and
        (item2.y - h2) < (item1.y + h1)
    )


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
                if is_touching(item1, item2):
                    item1.collided_with(item2)
                    item2.collided_with(item1)


    def remove_dead(self):
        for item in self.items[:]:
            if item.remove_from_game:
                self.remove(item)


    def update(self):
        self.detect_collisions()
        for item in self.items:
            if hasattr(item, 'update'):
                item.update()
            if hasattr(item, 'wraparound'):
                item.wraparound(self.win.width)
        self.remove_dead()

