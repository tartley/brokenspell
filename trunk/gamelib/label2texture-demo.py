import pyglet, code
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

    return texture.get_transform(flip_y=False)

window = pyglet.window.Window()
label = pyglet.text.Label('Hello World!',
  font_name = 'Times New Roman',
  font_size = 36,
  bold = True,
  x = 20,
  y = 5,
  color = (255, 0, 0, 255),
)
texture = label2texture(label)

glColor3f(1.0, 0.0, 1.0)

@window.event
def on_draw():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClearColor(0.0, 1.0, 0.0, 1.0)
    window.clear()
    texture.blit(200, 200)

pyglet.app.run()

