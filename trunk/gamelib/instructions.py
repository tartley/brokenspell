
from pyglet import clock
from pyglet.text import Label


class Instructions(object):

    def __init__(self,
        messages, x, y, anchor_x='center', anchor_y='center',
        delay=2, repeat=False, size=36):

        self.x = x
        self.y = y
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.delay = delay
        self.size = size
        self.repeat = repeat
        self.label = Label(
            '',
            font_size=self.size,
            x=self.x, y=self.y,
            anchor_x=self.anchor_x, anchor_y=self.anchor_y)

        self.set_messages(messages, delay=delay, repeat=repeat)


    def clear(self):
        if self.label:
            self.label.delete()
            self.label.text = ''
        clock.unschedule(self.next)


    def set_messages(self, messages, delay=2, repeat=False):
        self.clear()
        if isinstance(messages, basestring):
            messages = [messages]
        self.messages = messages
        self.delay=delay
        self.repeat = repeat
        self.msg_idx = 0
        self.next(None)


    def draw(self):
        if self.label.text:
            self.label.draw()


    def next(self, _):
        if self.msg_idx >= len(self.messages):
            if self.repeat:
                self.msg_idx = 0
            else:
                self.clear()
                return

        self.label.text = self.messages[self.msg_idx]
        self.msg_idx += 1
        if self.delay is not None:
            clock.schedule_once(self.next, self.delay)


