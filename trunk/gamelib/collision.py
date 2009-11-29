
from itertools import islice

from bird import Bird
from enemy import Enemy
from feather import Feather
from player import Player
from worlditem import WorldItem


collision_handlers = {
    (Player, Feather): Player.collide_feather,
    (Player, Enemy): Player.collide_enemy,
}

collision_handlers = {
    Player: {
        Feather: Player.collide_feather,
        Enemy: Player.collide_enemy,
    }
}



def is_touching(item1, item2):
    '''
    compare axis aligned rectangles, using item.width/height minus a border
    '''
    border = 6
    w1 = item1.width / 2 - border
    h1 = item1.height / 2 - border
    w2 = item2.width / 2 - border
    h2 = item2.height / 2 - border
    return (
        (item1.x - w1) < (item2.x + w2) and
        (item2.x - w2) < (item1.x + w1) and
        (item1.y - h1) < (item2.y + h2) and
        (item2.y - h2) < (item1.y + h1)
    )


class Collision(object):

    def _detect_type_collisions(self, items, type1, type2, handler):
        for index, item1 in enumerate(items[type1]):
            type2_items = items[type2]
            if type1 == type2:
                type2_items = islice(type2_items, index + 1, None)
            for item2 in type2_items:
                if is_touching(item1, item2):
                    handler(item1, item2)


    def detect(self, items):
        for type1, handlers in collision_handlers.iteritems():
            for type2, handler in handlers.iteritems():
                self._detect_type_collisions(items, type1, type2, handler)

