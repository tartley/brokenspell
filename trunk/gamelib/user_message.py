from pyglet.text import Label

class UserMessage(object):

    def __init__(self, width, height):
        self.label = None
        self.height = height
        self.width = width

    def set_message(self, text):
        if text:
            self.label = Label(text,
                               font_size=36,
                               x=self.width / 2,
                               y=self.height / 2,
                               anchor_x='center', anchor_y='center')
        else:
            if self.label is not None:
                self.label.delete()
                self.label = None


    def draw(self):
        if self.label is not None:
            self.label.draw()

