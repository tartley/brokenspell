
import math

from pyglet.window import key

from bird import Action, Bird
from feather import Feather
from hudmessage import HudMessage
from hudpoints import HudPoints, scores
from sounds import play


action_map = {
    key.Z:  Action.FLAP,
    key.LEFT: Action.LEFT,
    key.RIGHT: Action.RIGHT,
}


# TODO: Player *has-a* KeyStateHandler, doesn't need to *be* one
class Player(Bird, key.KeyStateHandler):

    is_player = True
    image_row = 3

    def __init__(self, x, y, game):
        Bird.__init__(self, x, y)
        self.game = game
        self.consecutive_feathers = 0


    @staticmethod
    def spawn(game):
        x = game.win.width / 2
        y = game.win.height + Player.height / 2
        game.add(Player(x, y, game))


    def think(self):
        if not self.is_alive:
            return set()

        actions = set()
        for keypress, action in action_map.iteritems():
            if self[keypress]:
                actions.add(action)
        return actions


    def collide_feather(self, feather):
        if feather.owner is self:
            return
        play('ding', self.consecutive_feathers)
        feather.remove_from_game = True
        idx = min(self.consecutive_feathers, len(scores) - 1)
        self.game.score += scores[idx]
        hudpoints = HudPoints(self.x, self.y, self.consecutive_feathers)
        self.game.add(hudpoints)
        self.consecutive_feathers += 1


    def collide_enemy(self, enemy):
        if self.is_alive and enemy.is_alive:
            Bird.bounce(self, enemy)
            self.consecutive_feathers = 0
            if self.y < enemy.y:
                self.hit(enemy)
            else:
                enemy.hit(self)


    def hit(self, _):
        Bird.die(self)
        play('die')
        play('ohno')
        self.game.add(HudMessage('Oh no!', 36))

