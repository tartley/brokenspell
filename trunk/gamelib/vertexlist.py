
from pyglet.gl import GL_QUADS, GL_TRIANGLES
from pyglet.graphics import OrderedGroup


class VertexList(object):
    """
    An item that can be added to the game world, and is rendered using
    a Pyglet IndexedVertexList. For example, the sky is a large GL_QUAD.
    """

    group = OrderedGroup(0)


    def __init__(self, verts, colors, primitive):
        self.verts = verts
        self.colors = colors
        self.primitive = primitive
        self.assert_valid()


    def assert_valid(self):
        assert self.num_verts == len(self.colors) / 3
        if self.primitive == GL_QUADS:
            assert self.num_verts % 4 == 0
        elif self.primitive == GL_TRIANGLES:
            assert self.num_verts % 3 == 0
        else:
            assert False # unvalidated primitive type


    @property
    def num_verts(self):
        return len(self.verts) / 2


    @property
    def indices(self):
        return xrange(self.num_verts)


    def get_batch_args(self):
        return (
            self.num_verts,
            self.primitive,
            self.group,
            self.indices,
            ('v2f/static', self.verts),
            ('c3B/static', self.colors)
        )

