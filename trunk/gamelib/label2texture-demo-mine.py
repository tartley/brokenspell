
import code
import pyglet
from pyglet.text import Label
from pyglet.gl import *


def label2texture(label):
    vertex_list = label._vertex_lists[0].vertices[:]
    xpos = map(int, vertex_list[::8])
    ypos = map(int, vertex_list[1::8])
    glyphs = label._get_glyphs()

    xstart = xpos[0]
    xend = xpos[-1] + glyphs[-1].width
    width = xend - xstart

    ystart = min(ypos)
    yend = max(ystart+glyph.height for glyph in glyphs)
    height = yend - ystart

    texture = pyglet.image.Texture.create(width, height, pyglet.gl.GL_ALPHA)

    for glyph, x, y in zip(glyphs, xpos, ypos):
        data = glyph.get_image_data()
        x = x - xstart
        y =  height - glyph.height - y + ystart
        texture.blit_into(data, x, y, 0)

    return texture


class Render(object):

    def create_image(self):
        label = pyglet.text.Label(
          text='yellow text',
          font_name = 'Times New Roman',
          font_size = 48,
          bold = True,
          x = 20,
          y = 5,
          color = (255, 255, 0, 255), # YELLOW
        )
        image = label2texture(label)

        # converting the Texture to an ImageData turns the text black
        # so don't do that
        # image = image.get_image_data()

        image.anchor_x = image.width / 2
        image.anchor_y = image.height / 2
        return image


    def init(self):
        self.win = pyglet.window.Window()
        self.win.on_draw = self.draw

        #glEnable(GL_BLEND)
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glClearColor(0.9, 0.5, 0.7, 0.0)

        self.image = self.create_image()

        pyglet.app.run()


    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.0, 0.0, 1.0) # current vertex color = blue

        # image displays text in the current vertex color?
        self.image.blit(self.win.width / 2, self.win.height / 2)


if __name__ == '__main__':
    r = Render()
    r.init()

