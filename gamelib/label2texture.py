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

    return texture


