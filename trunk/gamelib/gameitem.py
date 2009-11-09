
class GameItem(object):

    next_id = 0
    arena = None
    remove_from_game = False

    def __init__(self):
        self.id = GameItem.next_id
        GameItem.next_id += 1



