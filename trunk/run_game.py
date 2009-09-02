#! /usr/bin/env python

from gamelib.env import set_env_vars
set_env_vars()


from platform import system
from pyglet import options

if system() == 'Windows':
    options['audio'] = ('directsound', 'openal', 'silent')
else:
    options['audio'] = ('alsa', 'openal', 'silent')


from gamelib import main
main.main()

