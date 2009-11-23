
import math

from pyglet import clock, image

from config import settings
from collision import Collision
from enemy import Enemy
from event import Event
from feather import Feather
from worlditem import WorldItem


class Arena(object):

    def __init__(self, win, game):
        self.win = win
        self.game = game

        self.width = win.width
        self.height = win.height
        self.items = []

        self.item_added = Event()
        self.item_removed = Event()

        self.collision = Collision()


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


    def remove_dead(self):
        for item in self.items[:]:
            if item.remove_from_game:
                self.remove(item)


    def wraparound(self, item):
        if item.x < -item.width / 2:
            item.x += self.width + item.width
        if item.x > self.width + item.width / 2:
            item.x -= self.width + item.width


    def update(self):
        for item in self.items:
            if hasattr(item, 'update'):
                item.update()
        self.remove_dead()
        self.collision.detect(self.items)
        for item in self.items:
            if isinstance(item, WorldItem):
                self.wraparound(item)

