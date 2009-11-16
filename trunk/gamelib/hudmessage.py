
from pyglet import clock
from pyglet.text import Label

from gameitem import GameItem


class HudMessage(GameItem):

    render_layer = 3
    color = (255, 255, 255, 255)

    def __init__(self, text, size, x=None, y=None):
        GameItem.__init__(self)
        self.text = text
        self.size = size
        self.label = None
        if x is None:
            x = self.arena.win.width / 2
        self.x = x
        if y is None:
            y = self.arena.win.height / 2
        self.y = y


    def add_to_batch(self, batch, groups):
        self.label = Label(
            self.text,
            font_size=self.size,
            x=self.x, y=self.y,
            anchor_x='center', anchor_y='center',
            color=self.color,
            batch=batch,
            group=groups[self.render_layer] )

        def remove(_):
            self.remove_from_game = True

        clock.schedule_once(remove, 2)


    def remove_from_batch(self, batch):
        self.label.delete()


    def update(self):
        if self.label.text != self.text:
            self.label.text = self.text

