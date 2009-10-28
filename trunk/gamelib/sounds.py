from glob import glob
from os.path import join

from platform import system

from pyglet import options
from pyglet.media import load, Player

from gamelib.config import settings

sounds_dir = join('data', 'sounds')


def setup():
    force_audio = settings.get('all', 'force_audio')
    if force_audio:
        options['audio'] = (force_audio,)
    else:
        if system() == 'Windows':
            options['audio'] = ('directsound', 'openal', 'silent')
        else:
            options['audio'] = ('alsa', 'openal', 'silent')



music_source = None
music = None


def play_music(_):
    global music_source, music
    music_source = load(join('data', 'music3.ogg'))
    music = Player()
    music.volume = 0.15
    music.queue(music_source)
    music.eos_action = music.EOS_LOOP
    music.play()


def toggle_music():
    global music_source, music
    if music:
        if music.playing:
            music.pause()
        else:
            music.play()


def load_sound(name):
    return load(join(sounds_dir, name), streaming=False)


def load_sounds_matching(pattern):
    names = glob(join(sounds_dir, pattern))
    names.sort()
    return [load(n, streaming=False) for n in names]


quacks = load_sounds_matching('quack?.ogg')
dings = load_sounds_matching('ding?.ogg')
dies = load_sounds_matching('die?.ogg')
ohno = load_sound('ohno.ogg')
flap = load_sound('flap.ogg')

