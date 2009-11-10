
from gamelib.startup import startup
startup()


from pyglet import app
from gamelib.application import Application


def main():
    application = Application()
    app.run()

