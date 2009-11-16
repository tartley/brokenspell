
from pyglet import clock
from pyglet.text import Label

from hudmessage import HudMessage


class HudPoints(HudMessage):

    def __init__(self, *args):
        HudMessage.__init__(self, *args)
        self.bright = 255
        self.dy = 2.0


    def update(self):
        self.label.y += self.dy
        self.dy *= 0.98
        self.bright -= 2
        self.label.color = (255, 255, 200, self.bright)

