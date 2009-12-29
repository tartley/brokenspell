#! /usr/bin/env python

import cProfile

import fixpath

from gamelib.startup import startup

command = 'startup()'
cProfile.runctx(command, globals(), locals(), filename='profile.out')

