
import locale

from pyglet.text import Label

from .hudmessage import HudMessage
from .player import Player


class HudScore(HudMessage):

    def __init__(self, *args, **kwargs):
        kwargs.update(dict(
            anchor_x = 'right',
            anchor_y = 'top',
            x = self.game.width - 10,
            y = self.game.height - 5,
        ))
        HudMessage.__init__(self, self.text, *args, **kwargs)


    @property
    def source(self):
        return Player.score


    @property
    def text(self):
        locale.setlocale(locale.LC_ALL, "")
        return locale.format('%d', self.source, True)

