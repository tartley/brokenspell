
import math

from pyglet import clock
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


class Player(Bird):

    is_player = True
    score = 0

    def __init__(self, x, y):
        Bird.__init__(self, x, y)
        self.consecutive_feathers = 0


    @staticmethod
    def get_ready():
        Player.game.add(HudMessage('Get Ready!', 36))
        clock.schedule_once(lambda _: Player.spawn(), 1)


    @staticmethod
    def spawn():
        x = Player.game.width / 2
        y = Player.game.height + Player.height / 2
        Player.game.add(Player(x, y))


    def removed(self):
        clock.schedule_once(lambda _: Player.get_ready(), 1.5)


    # TODO,impliment Player.think() as a behaviour think state
    # and have it replaced with 'plummet' on death, just like enemy is
    def think(self):
        if not self.is_alive:
            return set()

        actions = set()
        for keypress, action in action_map.iteritems():
            if self.game.keystate[keypress]:
                actions.add(action)
        return actions


    def collide_feather(self, feather):
        if feather.owner is self:
            return
        play('ding', self.consecutive_feathers)
        feather.remove_from_game = True
        idx = min(self.consecutive_feathers, len(scores) - 1)
        Player.score += scores[idx]
        hudpoints = HudPoints(self.x, self.y, self.consecutive_feathers)
        self.game.add(hudpoints)
        self.consecutive_feathers += 1


    def collide_enemy(self, enemy):
        if self.is_alive and enemy.is_alive:
            Bird.bounce(self, enemy)
            if self.y < enemy.y:
                self.hit(enemy)
            else:
                enemy.hit(self)
                self.consecutive_feathers = 0


    def hit(self, _):
        Bird.die(self)
        play('die')
        play('ohno')
        self.game.add(HudMessage('Oh no!', 36))

