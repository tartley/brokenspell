
from pyglet import clock
from pyglet.window import key
from pyglet.text import Label

from hudmessage import HudMessage


texts = [
    'Press Z to flap',
    '',
    'Left and Right to steer',
    '',
]

all_done = [
    set(), set([key.LEFT]), set([key.RIGHT])
]


class HudInstructions(HudMessage):

    color = (255, 255, 255, 127)

    def __init__(self, *args, **kwargs):
        kwargs.update(dict(
            anchor_x = 'right',
            anchor_y = 'bottom',
            x = self.game.width - 10,
            y = 5,
            font_size = 24,
        ))
        self.textidx = -1
        HudMessage.__init__(self, self.text, *args, **kwargs)
        self.need_pressing = set([key.LEFT, key.RIGHT, key.Z])


    @property
    def source(self):
        return texts[self.textidx]


    def add_to_batch(self, batch, groups):
        HudMessage.add_to_batch(self, batch, groups)
        clock.schedule_once(self.next_text, 5)


    def remove_from_batch(self, batch):
        HudMessage.remove_from_batch(self, batch)
        clock.unschedule(self.next_text)


    def next_text(self, _):
        self.textidx += 1
        self.textidx %= len(texts)
        delay = 1.5
        if self.text == '':
            delay = 0.5
        clock.schedule_once(self.next_text, delay)


    def on_key_press(self, symbol, __):
        if symbol in self.need_pressing:
            self.need_pressing.remove(symbol)
        if self.need_pressing in all_done:
            self.remove_from_game = True

