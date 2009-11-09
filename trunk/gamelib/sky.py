
from pyglet.gl import GL_QUADS

from gameitem import GameItem
from vertexlist import VertexList


class Sky(GameItem):

    def __init__(self, width, height):
        verts = (
            width, height,
            0, height,
            0, 0,
            width, 0,
        )
        colors = (
            000, 000, 127,
            000, 000, 127,
            064, 127, 255,
            064, 127, 255,
        )
        self.vertexlist = VertexList(verts, colors, GL_QUADS)

