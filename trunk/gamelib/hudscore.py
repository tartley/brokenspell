
from pyglet.text import Label

from gameitem import GameItem


class HudScore(GameItem):

    render_layer = 3

    def __init__(self, game, screen_width, screen_height):
        self.game = game
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.label = None


    @property
    def text(self):
        return str(self.game.score)


    def add_to_batch(self, batch, groups, _):
        self.label = Label(
            self.text,
            font_size=36,
            x=self.screen_width - 10, y=self.screen_height - 5,
            anchor_x='right', anchor_y='top',
            batch=batch,
            group=groups[self.render_layer] )


    def remove_from_batch(self, batch):
        self.label.delete()


    def update(self):
        if self.label and self.label.text != self.text:
            self.label.text = self.text

