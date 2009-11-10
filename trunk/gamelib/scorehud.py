
from gameitem import GameItem


class ScoreHud(GameItem):

    render_layer = 3

    def __init__(self, game, width, height):
        self.game = game
        self.label = None
        self.font_size = 36
        self.x = width - 10
        self.y = height - 5
        self.anchor_x = 'right'
        self.anchor_y = 'top'


    @property
    def text(self):
        return str(self.game.score)


    def update(self):
        if self.label.text != self.text:
            self.label.text = self.text

