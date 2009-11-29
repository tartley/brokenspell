
from pyglet import clock

from collision import Collision
from enemy import Enemy
from event import Event
from stresstest import StressTest
from feather import Feather
from gameitem import GameItem
from ground import Ground
from hudgameover import HudGameOver
from hudlives import HudLives
from hudmessage import HudMessage
from hudscore import HudScore
from hudtitle import HudTitle
from hudinstructions import HudInstructions
from player import Player
from sky import Sky
from typebag import TypeBag
from worlditem import WorldItem



class Game(object):

    def __init__(self, keystate, width, height):
        self.keystate = keystate
        self.width = width
        self.height = height
        self.wave = 0
        self._items = TypeBag()
        self.item_added = Event()
        self.item_removed = Event()
        self._to_be_added = []
        self.collision = Collision()
        GameItem.game = self


    def __iter__(self):
        return iter(self._items)


    def add(self, item):
        self._to_be_added.append(item)


    def _add(self, item):
        self._items.add(item)
        item.added()
        self.item_added(item)


    def remove(self, item=None, itemid=None):
        assert (item is None) ^ (itemid is None)
        if item is None:
            item = self._items[itemid]
        self._items.remove(item)

        item.removed()
        self.item_removed(item)


    def startup(self):
        self.add(Sky())
        self.add(Ground())
        self.add(StressTest())
        self.add(HudLives())
        self.add(HudScore())
        clock.schedule(self.update)
        self.title()


    def title(self):
        self.add(HudTitle())


    def _remove_last_games_items(self):
        for itemtype in (Enemy, Feather):
            for item in self._items[itemtype]:
                item.remove_from_game = True


    def start(self):
        self._remove_last_games_items()

        self.wave = 0
        Player.get_ready()
        Player.score = 0
        Player.lives = 3
        self.add(HudInstructions())
        clock.schedule_once(lambda _: self.spawn_wave(), 3)


    def over(self):
        self.add(HudGameOver())


    def spawn_wave(self):
        self.wave += 1
        self.add(HudMessage('Wave %d' % (self.wave,)))

        number = self.wave ** 2
        for n in xrange(number):
            clock.schedule_once(
                lambda _: Enemy.spawn(self),
                n * 0.25)


    def wraparound(self, item):
        if item.x < -item.width / 2:
            item.x += self.width + item.width
        if item.x > self.width + item.width / 2:
            item.x -= self.width + item.width


    def update(self, _):
        # iterate through self._items, updating each
        ids_to_remove = set()
        for item in self._items:
            item.update()
            if item.remove_from_game:
                ids_to_remove.add(id(item))
            # TODO, can we find a way to iterate through WorldItems?
            if isinstance(item, WorldItem):
                self.wraparound(item)

        # Add and remove from self._items here
        while self._to_be_added:
            self._add(self._to_be_added.pop())
        for itemid in ids_to_remove:
            self.remove(itemid=itemid)

        self.collision.detect(self._items)

