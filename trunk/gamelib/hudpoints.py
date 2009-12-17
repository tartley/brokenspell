
from pyglet.text import Label

from label2texture import label2texture
from spriteitem import SpriteItem


class HudPoints(SpriteItem):
    '''
    Represents a number floating in the sky, instanciated whenever the player
    scores some points.

    For performance, we generate bitmaps from each label, and blit the bitmap in
    the batch, instead of the label itself.
    '''

    render_layer = 3 # hud

    def __init__(self, x, y, score):
        SpriteItem.__init__(self, x, y)
        size = 16 + score / 10
        label = Label(
            text=str(score),
            font_size = size)
        image = label2texture(label)
        image.anchor_x = image.width / 2
        image.anchor_y = image.height / 2
        self.images = [image]

        self.dy = 2 + score / 50
        self.opacity = 255


    def update(self):
        self.y += self.dy
        self.dy *= 0.9
        self.sprite.opacity = self.opacity
        self.opacity -= 3
        if self.opacity <= 0:
            self.remove_from_game = True

