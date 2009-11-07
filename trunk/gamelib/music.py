
from os.path import join

from pyglet import clock
from pyglet.media import load, Player

from gamelib.config import settings


class Music(object):

    def __init__(self):
        self.music = None
        self.player = None


    def play(self):
        if settings.get('all', 'force_audio') == 'silent':
            return

        self.music = load(join('data', 'music3.ogg'))
        self.player = Player()
        self.player.volume = 0.15
        self.player.queue(self.music)
        self.player.eos_action = self.player.EOS_LOOP

        # if we play music immediately, it stutters a little at the start
        # so schedule it to start a second from now
        if settings.getboolean('all', 'music'):
            clock.schedule_once(lambda _: self.player.play(), 1)


    def toggle(self):
        if settings.get('all', 'force_audio') == 'silent':
            return

        if self.player:
            if self.player.playing:
                self.player.pause()
            else:
                self.player.play()

