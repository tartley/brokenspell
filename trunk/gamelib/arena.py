
import math

from pyglet import clock, image

from collision import Collision
from config import settings
from enemy import Enemy
from event import Event
from feather import Feather
from typebag import TypeBag
from worlditem import WorldItem


# TODO: this class perhaps redundant now
# TypeBag can fire events when items are added and removed
# pushing handlers can be done by Application listening for those events
# wraparound and update are Game methods
# The only thing stopping me is the Game is already my biggest 'god class'
class Arena(object):

    def __init__(self, win, game):
        self.win = win
        self.game = game

        self.items = TypeBag()

        self.item_added = Event()
        self.item_removed = Event()

        self.collision = Collision()


    def add(self, item):
        self.items.add(item)

        if hasattr(item, 'on_key_press'):
            self.win.push_handlers(item)

        self.item_added(self, item)


    def remove(self, item=None, itemid=None):
        item = self.items.remove(item, itemid)

        if hasattr(item, 'on_key_press'):
            self.win.remove_handlers(item)

        self.item_removed(self, item)


    def wraparound(self, item):
        if item.x < -item.width / 2:
            item.x += self.win.width + item.width
        if item.x > self.win.width + item.width / 2:
            item.x -= self.win.width + item.width


    def update(self):
        to_remove = set()
        for item in self.items:
            if hasattr(item, 'update'):
                item.update()
            if item.remove_from_game:
                to_remove.add(id(item))

        for itemid in to_remove:
            self.remove(itemid=itemid)

        self.collision.detect(self.items)

        # TODO, can we find a way to iterate through WorldItems?
        for item in self.items:
            if isinstance(item, WorldItem):
                self.wraparound(item)

