#! /usr/bin/env python


def main():
    from gamelib.startup import startup
    startup()

    from gamelib.application import Application
    Application().run()


if __name__ == '__main__':
    main()

