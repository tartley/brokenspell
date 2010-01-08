
from pyglet.text import Label

from .hudmessage import HudMessage
from .player import Player


class HudLives(HudMessage):

    def __init__(self, *args, **kwargs):
        kwargs.update(dict(
            anchor_x = 'right',
            anchor_y = 'top',
            x = self.game.width - 10,
            y = self.game.height - 50,
            color = (255, 255, 255, 127),
        ))
        HudMessage.__init__(self, self.text, *args, **kwargs)

    @property
    def source(self):
        return Player.lives

    @property
    def text(self):
        return '*' * self.source

