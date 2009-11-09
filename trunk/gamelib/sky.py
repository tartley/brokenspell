
from pyglet.gl import GL_QUADS

from gameitem import GameItem
from vertexlist import VertexList


class Sky(GameItem):

    render_layer = 0

    def __init__(self, width, height):
        self.verts = (
            width, height,
            0, height,
            0, 0,
            width, 0,
        )
        self.colors = (
            000, 000, 127,
            000, 000, 127,
            064, 127, 255,
            064, 127, 255,
        )
        self.vertexlist = None

