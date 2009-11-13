
from pyglet import clock
from pyglet.window import key
from pyglet.text import Label

from gameitem import GameItem


text = [
    'Left and Right to steer',
    'Press Z to flap',
]

all_done = [
    set(), set([key.LEFT]), set([key.RIGHT])
]


class HudInstructions(GameItem):

    render_layer = 3

    def __init__(self, _, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.label = None
        self.textidx = 0
        self.need_pressing = set([key.LEFT, key.RIGHT, key.Z])


    def add_to_batch(self, batch, groups, _):
        self.label = Label(
            text[self.textidx],
            font_size=36,
            x=10, y=self.screen_height - 5,
            anchor_x='left', anchor_y='top',
            batch=batch,
            group=groups[self.render_layer] )
        self.next_text(None)


    def remove_from_batch(self, batch):
        self.label.delete()
        self.label = None
        clock.unschedule(self.next_text)


    def next_text(self, _):
        self.textidx += 1
        self.textidx %= len(text)
        self.label.text = text[self.textidx]
        clock.schedule_once(self.next_text, 1.5)


    def on_key_press(self, symbol, __):
        if symbol in self.need_pressing:
            self.need_pressing.remove(symbol)
        if self.need_pressing in all_done:
            self.remove_from_game = True
