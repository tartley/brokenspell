#! /usr/bin/env python

from gamelib.env import set_env_vars
set_env_vars()

from pyglet import options
options['audio'] = ('alsa', 'openal', 'silent')

from gamelib import main
main.main()

