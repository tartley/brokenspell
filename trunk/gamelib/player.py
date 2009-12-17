
import math

from pyglet import clock
from pyglet.window import key

from bird import Action, Bird
from feather import Feather
from hudmessage import HudMessage
from hudpoints import HudPoints
from sounds import play


action_map = {
    key.Z:  Action.FLAP,
    key.LEFT: Action.LEFT,
    key.RIGHT: Action.RIGHT,
}

MULTIPLIER_DELAY = 3


class Player(Bird):

    is_player = True
    score = 0
    multiplier = 1
    lives = 0

    def __init__(self, x, y):
        Bird.__init__(self, x, y)
        self.consecutive_enemies = 0


    @staticmethod
    def start_game():
        Player.get_ready()
        Player.score = 0
        Player.lives = 3
        Player.multiplier = 1


    @staticmethod
    def get_ready():
        Player.game.add(HudMessage('Get Ready!', remove_after=2))
        clock.schedule_once(lambda _: Player.spawn(), 1)


    @staticmethod
    def spawn():
        x = Player.game.width / 2
        y = Player.game.height + Player.height / 2
        Player.game.add(Player(x, y))


    def removed(self):
        Player.lives -= 1
        if Player.lives == 0:
            clock.schedule_once(lambda _: self.game.over(), 1.5)
        else:
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
        feather.remove_from_game = True
        play('ding', self.multiplier - 1)
        self._increment_multiplier()
        self.consecutive_enemies = 0


    def _increment_multiplier(self):
        Player.multiplier += 1
        clock.unschedule(self._decrement_multiplier)
        clock.schedule_once(self._decrement_multiplier, MULTIPLIER_DELAY)


    def _decrement_multiplier(self, _):
        if Player.multiplier > 1:
            Player.multiplier -= 1
            if Player.multiplier > 1:
                clock.schedule_once(
                    self._decrement_multiplier, MULTIPLIER_DELAY)


    def collide_enemy(self, enemy):
        if self.is_alive and enemy.is_alive:
            Bird.bounce(self, enemy)
            if self.y < enemy.y:
                self.hit(enemy)
            else:
                enemy.hit(self)
                self.consecutive_enemies += 1
                points = self.consecutive_enemies * 10 * self.multiplier
                Player.score += points
                self.game.add( HudPoints(self.x, self.y, points) )


    def hit(self, _):
        Bird.die(self)
        play('die')
        play('ohno')
        self.game.add(HudMessage('Oh no!', remove_after=2))


