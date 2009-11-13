#! /usr/bin/env python


def main():
    # startup() must happen before pyglet is imported

    from gamelib.startup import startup
    startup()

    from gamelib.application import Application
    import pyglet
    Application()
    pyglet.app.run()


if __name__ == '__main__':
    main()

