from pyglet import clock
from pyglet.text import Label


MESSAGES = [
        "ESC to exit",
        "Left and right to move around",
        "Z flaps wings",
        "Catch feathers to increase flap strength",
        ""
]


class Instructions(object):

    def __init__(self):
        self.instruction = None
        self.showing_message = 0
        for number, message in enumerate(MESSAGES):
            clock.schedule_once(lambda _: self.change_text(), 3*number)


    def draw(self):
        if self.instruction:
            self.instruction.y = self.instruction_pos.next()
            self.instruction.draw()


    def change_text(self):
        message = MESSAGES[self.showing_message]
        self.showing_message += 1
        self.instruction = Label(message,
                font_size=36, x=1024, y=0,
                anchor_x='right', anchor_y='top')
        self.instruction.y = 0
        def set_pos(pos):
            while pos <= self.instruction.content_height:
                pos += 1
                yield pos
            while 1:
                yield self.instruction.content_height
        self.instruction_pos = set_pos(0)


