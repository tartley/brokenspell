
from pyglet.text import Label

from .hudmessage import HudMessage
from .player import Player

colors = [
    (127, 127, 255, 127),
    (127, 255, 255, 127),
    (127, 255, 127, 127),
    (255, 255, 127, 127),
    (255, 127, 127, 127),
    (255, 127, 255, 127),
    (127, 127, 255, 255),
    (127, 255, 255, 255),
    (127, 255, 127, 255),
    (255, 255, 127, 255),
    (255, 127, 127, 255),
    (255, 127, 255, 255),
    (255, 255, 255, 255),
]

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
        if Player.multiplier:
            return Player.multiplier.value
        return 0

    @property
    def text(self):
        if Player.multiplier:
            return 'x%d' % (Player.multiplier.value, )
        return ''


    def update(self, _):
        self.label.begin_update()
        self.label.font_size = 24 + self.source * 3
        self.label.color = colors[min(self.source, len(colors)) - 1]
        HudMessage.update(self, None)
        self.label.end_update()

