
from gamelib.env import set_env_vars
set_env_vars()

from pyglet import app

from gamelib.application import Application
from gamelib.sounds import setup


def main():
    setup()
    application = Application()
    app.run()

