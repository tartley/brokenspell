
from pyglet.text import Label

from hudmessage import HudMessage
from player import Player


class HudMultiplier(HudMessage):

    # TODO, change color depending on value of multiplier

    def __init__(self, *args, **kwargs):
        kwargs.update(dict(
            anchor_x = 'left',
            anchor_y = 'top',
            x = 10,
            y = self.game.height - 5,
            font_size = 24,
            color = (255, 255, 255, 127),
        ))
        HudMessage.__init__(self, self.text, *args, **kwargs)

    @property
    def source(self):
        return Player.multiplier

    @property
    def text(self):
        return 'x%d' % (Player.multiplier, )

