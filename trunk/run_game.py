#! /usr/bin/env python

from gamelib.config import settings
from gamelib.env import set_env_vars
set_env_vars()

from platform import system
from pyglet import options

force_audio = settings.get('all', 'force_audio')
if force_audio:
    options['audio'] = (force_audio,)
else:
    if system() == 'Windows':
        options['audio'] = ('directsound', 'openal', 'silent')
    else:
        options['audio'] = ('alsa', 'openal', 'silent')


from gamelib import main
main.main()

