
from pyglet import resource
from pyglet.sprite import Sprite


class Player(object):

    def __init__(self):
        self.x = self.y = 0

        image = resource.image('data/images/Player-flap.png')
        self.sprite = Sprite(image)

    def draw(self):
        self.sprite.position = (self.x, self.y)
        self.sprite.draw()

