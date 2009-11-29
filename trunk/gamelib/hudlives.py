
from pyglet.text import Label

from gameitem import GameItem
from player import Player


class HudLives(GameItem):

    render_layer = 3

    def __init__(self):
        GameItem.__init__(self)
        self.label = None
        self.old_source = None

    @property
    def source(self):
        return Player.lives

    @property
    def text(self):
        return '*' * self.source

    def add_to_batch(self, batch, groups):
        self.label = Label(
            self.text,
            font_size=36,
            color = (255, 255, 255, 127),
            x=self.game.width - 10, y=self.game.height - 50,
            anchor_x='right', anchor_y='top',
            batch=batch,
            group=groups[self.render_layer],
        )
        self.old_source = self.source

    def remove_from_batch(self, batch):
        self.label.delete()

    def update(self):
        if self.source != self.old_source:
            self.label.text = self.text
            self.old_source = self.source

