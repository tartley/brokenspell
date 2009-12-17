
from pyglet import clock
from pyglet.text import Label

from gameitem import GameItem


class HudMessage(GameItem):

    render_layer = 3
    color = (255, 255, 255, 255)

    def __init__(self,
        text,
        font_size=36,
        x=None, y=None,
        anchor_x='center', anchor_y='center',
        font_name=None,
        color=None,
        remove_after=None,
    ):
        GameItem.__init__(self)
        self._text = text
        self.font_size = font_size
        if x is None:
            x = self.game.width / 2
        self.x = x
        if y is None:
            y = self.game.height / 2
        self.y = y
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.font_name = font_name
        if color is None:
            color = HudMessage.color
        self.color = color
        self.label = None
        # used to detect when Label needs updating
        self.old_source = None
        # message removes itself from game after this many seconds
        self.remove_after = remove_after


    @property
    def text(self):
        return self.source


    @property
    def source(self):
        return self._text


    def add_to_batch(self, batch, groups):
        self.label = Label(
            self.text,
            font_name=self.font_name,
            font_size=self.font_size,
            x=self.x, y=self.y,
            anchor_x=self.anchor_x, anchor_y=self.anchor_y,
            color=self.color,
            batch=batch,
            group=groups[self.render_layer]
        )
        self.old_source = self.source

        def remove(_):
            self.remove_from_game = True

        if self.remove_after:
            clock.schedule_once(remove, self.remove_after)


    def remove_from_batch(self, batch):
        self.label.delete()


    def update(self):
        if self.source != self.old_source:
            self.label.text = self.text
            self.old_source = self.source

