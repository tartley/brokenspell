
class GameItem(object):

    next_id = 0
    arena = None

    def __init__(self):
        self.id = GameItem.next_id
        GameItem.next_id += 1
        self.remove_from_game = False


    def __str__(self):
        return "<%s%s>" % (type(self).__name__, self.id)

