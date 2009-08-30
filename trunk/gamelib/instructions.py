from pyglet import clock
from pyglet.text import Label


MESSAGES = [
        "Sinister Ducks",
        "ESC to exit",
        "Left and right to move around",
        "Z flaps wings",
        "Catch feathers to increase flap strength",
        None
]


class Instructions(object):

    def __init__(self):
        self.instruction = None
        self.showing_message = 0
        for number, message in enumerate(MESSAGES):
            clock.schedule_once(lambda _: self.change_text(), 3*number)


    def draw(self):
        if self.instruction:
            self.instruction.draw()


    def change_text(self):
        message = MESSAGES[self.showing_message]
        if not message:
            self.instruction = None
            return
        self.showing_message += 1
        self.instruction = Label(message,
                font_size=36, x=1024, y=0,
                anchor_x='right', anchor_y='top')
        self.instruction.y = 0
        def set_pos():
            if self.instruction and self.instruction.y <= self.instruction.content_height:
                self.instruction.y += 1
        clock.schedule(lambda _: set_pos())


