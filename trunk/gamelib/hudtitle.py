
from pyglet import clock
from pyglet.text import Label
from pyglet.window import key

from gameitem import GameItem


colors = [
    (255, 255, 255, 128),
    (255, 255, 255, 0),
]


class HudTitle(GameItem):

    render_layer = 3

    def __init__(self):
        GameItem.__init__(self)
        self.titleLabel = None
        self.pressAnyKeyLabel = None


    def add_to_batch(self, batch, groups):
        self.titleLabel = Label(
            'Sinister Ducks',
            font_size=36,
            x=self.game.width / 2, y=self.game.height / 2 + 30,
            anchor_x='center', anchor_y='center',
            batch=batch,
            group=groups[self.render_layer] )
        self.pressAnyKeyLabel = Label(
            'Press any key',
            font_size=18,
            x=self.game.width / 2, y=self.game.height / 2 - 20,
            anchor_x='center', anchor_y='center',
            batch=batch,
            group=groups[self.render_layer] )
        self.blink(None)


    def remove_from_batch(self, batch):
        self.titleLabel.delete()
        self.titleLabel = None
        self.pressAnyKeyLabel.delete()
        self.pressAnyKeyLabel = None
        clock.unschedule(self.blink)


    def blink(self, _):
        blink = self.pressAnyKeyLabel.color == colors[0]
        self.pressAnyKeyLabel.color = colors[blink]
        clock.schedule_once(self.blink, 0.4 + 0.2 * blink)


    def on_key_press(self, _, __):
        clock.schedule_once(lambda _: self.game.start(), 1)
        self.remove_from_game = True


