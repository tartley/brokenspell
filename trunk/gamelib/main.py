
from pyglet import app

from gamelib.pre_run import pre_run
pre_run()

from gamelib.application import Application

def main():
    application = Application()
    app.run()

