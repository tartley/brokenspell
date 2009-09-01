
from pyglet import clock
from pyglet.text import Label



class Instructions(object):

    def __init__(self, messages, x, y, anchor_x, anchor_y):
        self.messages = messages
        self.x = x
        self.y = y
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.instruction = None
        self.msg_idx = 0
        for number, message in enumerate(self.messages):
            clock.schedule_once(lambda _: self.change_text(), 3*number)


    def draw(self):
        if self.instruction:
            self.instruction.draw()


    def change_text(self):
        message = self.messages[self.msg_idx]
        if not message:
            self.instruction = None
            return
        self.msg_idx += 1
        self.instruction = Label(message,
                font_size=36, x=1024, y=0,
                anchor_x='right', anchor_y='top')
        self.instruction.y = 0

        def set_pos():
            if (self.instruction and 
                self.instruction.y <= self.instruction.content_height):

                self.instruction.y += 1

        clock.schedule(lambda _: set_pos())


