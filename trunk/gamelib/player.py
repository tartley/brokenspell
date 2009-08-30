
from pyglet import resource
from pyglet.sprite import Sprite
from pyglet.window import key


class Player(object):

    def __init__(self):
        self.x = self.y = 0

        image = resource.image('data/images/Player-flap.png')
        self.sprite = Sprite(image)


    def read_controls(self, keyhandler):
        if keyhandler[key.LEFT]:
            self.x -= 1
        if keyhandler[key.RIGHT]:
            self.x += 1
            

    def draw(self):
        self.sprite.position = (self.x, self.y)
        self.sprite.draw()

