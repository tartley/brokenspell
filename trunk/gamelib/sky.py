
from pyglet.gl import GL_QUADS

from vertexlist import VertexList
from gameitem import GameItem


class Sky(GameItem):

    render_layer = 0

    def __init__(self, width, height):
        GameItem.__init__(self)
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


    def add_to_batch(self, batch, groups):
        # TODO: add_indexed returns a vertexlist. It is this we should be
        # deleting to remove from batch. We must rename VertexList to
        # something else.
        self.vertexlist = VertexList(self.verts, self.colors, GL_QUADS)
        batch.add_indexed(
            self.vertexlist.num_verts,
            self.vertexlist.primitive,
            groups[self.render_layer],
            self.vertexlist.indices,
            ('v2f/static', self.vertexlist.verts),
            ('c3B/static', self.vertexlist.colors) )

    def remove_from_batch(self):
        raise Exception('not implimented')

