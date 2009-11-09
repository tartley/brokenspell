
from gameitem import GameItem


class Ground(GameItem):

    render_layer = 1

    def __init__(self):
        GameItem.__init__(self)
        self.sprite = None

