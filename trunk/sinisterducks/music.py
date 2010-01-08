
from os.path import join

from pyglet import clock

from .config import settings


load = None
Player = None


class Music(object):

    def __init__(self):
        self.music = None
        self.player = None


    def load(self):
        try:
            global load, Player
            from pyglet import media
            load = media.load
            Player = media.Player
            self.music = load(join('data', 'music3.ogg'))
        except Exception:
            print "WARNING: can't start music"
            settings.set('all', 'force_audio', 'silent')


    def play(self):
        if settings.get('all', 'force_audio') == 'silent':
            return

        self.player = Player()
        self.player.volume = 0.15
        self.player.eos_action = self.player.EOS_LOOP
        self.player.queue(self.music)

        # if we play music immediately, it stutters a little at the start
        # so schedule it to start a second from now
        if settings.getboolean('all', 'music'):
            clock.schedule_once(lambda _: self.player.play(), 1)


    def toggle(self):
        if self.player and settings.get('all', 'force_audio') != 'silent':
            if self.player.playing:
                self.player.pause()
            else:
                self.player.play()
