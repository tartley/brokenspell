
from itertools import islice

from worlditem import WorldItem


def is_touching(item1, item2):
    '''
    compare axis aligned rectangles, size of item.width/height minus a border
    '''
    if not isinstance(item1, WorldItem) or not isinstance(item2, WorldItem):
        return False
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

    def detect(self, items):
        for i, item1 in enumerate(items):
            for item2 in islice(items, i+1, None):
                if is_touching(item1, item2):
                    item1.collided_with(item2)
                    item2.collided_with(item1)

