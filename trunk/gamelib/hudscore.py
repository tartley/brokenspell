
from pyglet.text import Label

from gameitem import GameItem


class HudScore(GameItem):

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


    def add_to_batch(self, batch, groups, _):
        self.label = Label(
            self.text,
            font_size=self.font_size,
            x=self.x, y=self.y,
            anchor_x=self.anchor_x, anchor_y=self.anchor_y,
            batch=batch,
            group=groups[self.render_layer] )


    def remove_from_batch(self, batch):
        self.label.delete()

