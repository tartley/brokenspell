
from pyglet import clock
from pyglet.text import Label

from gameitem import GameItem


class HudMessage(GameItem):

    render_layer = 3

    def __init__(self, text, game, screen_width, screen_height):
        self.text = text
        self.game = game
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.label = None


    def add_to_batch(self, batch, groups, _):
        self.label = Label(
            self.text,
            font_size=36,
            x=self.screen_width / 2, y=self.screen_height / 2,
            anchor_x='center', anchor_y='center',
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

