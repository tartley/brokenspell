
from hudmessage import HudMessage

class HudGameOver(HudMessage):

    def __init__(self):
        HudMessage.__init__(self, 'Game Over', remove_after=4)

    def removed(self):
        HudMessage.removed(self)
        self.game.title()

    def on_key_press(self, _, __):
        self.remove_from_game = True

