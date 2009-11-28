
class GameItem(object):

    game = None
    win = None

    def __init__(self):
        self.remove_from_game = False


    def added(self):
        if hasattr(self, 'on_key_press'):
            self.win.push_handlers(self)


    def removed(self):
        if hasattr(self, 'on_key_press'):
            self.win.remove_handlers(self)


    def update(self):
        pass

