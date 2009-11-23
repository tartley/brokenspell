
import code
import pyglet


class StringTextureAtlas:
    _glyph_cache = dict()

    def __init__(self, width=1024, height=1024, format=pyglet.gl.GL_ALPHA):
        self.texture = pyglet.image.Texture.create(width, height, format)
        self.allocator = pyglet.image.atlas.Allocator(width, height)

    def region(self, width, height):
        x, y = self.allocator.alloc(width, height)
        return self.texture.get_region(x, y, width, height)

    def label(self, *args, **kwargs):
        label = pyglet.text.Label(*args, **kwargs)

        vertex_list = label._vertex_lists[0].vertices[:]
        xpos = map(int, vertex_list[::8])
        ypos = map(int, vertex_list[1::8])
        glyphs = label._get_glyphs()

        xstart = xpos[0]
        xend = xpos[-1] + glyphs[-1].width
        width = xend - xstart

        ystart = min(ypos)
        yend = max(y+glyph.height for y, glyph in zip(ypos, glyphs))
        height = yend - ystart

        texture = self.region(width, height)

        for glyph, x, y in zip(glyphs, xpos, ypos):
            data = self._glyph_cache.get(glyph)
            if not data:
                data = self._glyph_cache[glyph] = glyph.get_image_data()
            x = x - xstart
            y = height - glyph.height - y + ystart
            texture.blit_into(data, x, y, 0)

        return texture.get_transform()

