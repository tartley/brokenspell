
import locale

from pyglet.text import Label

from gameitem import GameItem
from player import Player


class HudScore(GameItem):

    render_layer = 3

    def __init__(self):
        GameItem.__init__(self)
        self.label = None
        self.old_source = None


    @property
    def source(self):
        return Player.score


    @property
    def text(self):
        locale.setlocale(locale.LC_ALL, "")
        return locale.format('%d', self.source, True)


    def add_to_batch(self, batch, groups):
        self.label = Label(
            self.text,
            font_size=36,
            x=self.game.width - 10, y=self.game.height - 5,
            anchor_x='right', anchor_y='top',
            batch=batch,
            group=groups[self.render_layer] )
        self.old_source = self.source


    def remove_from_batch(self, batch):
        self.label.delete()


    def update(self):
        if self.source != self.old_source:
            self.label.text = self.text
            self.old_source = self.source

