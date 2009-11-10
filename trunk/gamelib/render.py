
from pyglet import clock
from pyglet.gl import (
    glBlendFunc, glEnable,
    GL_BLEND, GL_ONE_MINUS_SRC_ALPHA, GL_QUADS, GL_SRC_ALPHA,
)
from pyglet.graphics import Batch, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.text import Label

from graphics import Graphics
from vertexlist import VertexList


class Render(object):

    groups = [
        OrderedGroup(0), # sky
        OrderedGroup(1), # hills
        OrderedGroup(2), # birds & feathers
        OrderedGroup(3), # hud
    ]

    # TODO: we don't need to pass application or win here
    # just arena would be fine
    # uses of win in clear will go away when background is a gameitem
    def __init__(self, application, win):
        self.application = application
        self.win = win
        self.images = None

        self.application.arena.item_added += self.add_item_to_batch
        self.application.arena.item_removed += self.remove_item_from_batch

        self.clockDisplay = clock.ClockDisplay()
        self.batch = Batch()


    def init(self, win):
        graphics = Graphics()
        self.images = graphics.load()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    def draw(self):
        for item in self.application.arena.items:
            if hasattr(item, 'animate'):
                item.animate(self.images)

        self.batch.draw()

        self.application.user_message.draw()
        self.application.instructions.draw()
        self.clockDisplay.draw()


    def create_item_sprite(self, item):
        item.sprite = Sprite(
            self.images[item.__class__.__name__][0],
            batch=self.batch,
            group=self.groups[item.render_layer] )
        item.update_sprite_stats()


    def create_item_vertexlist(self, item):
        item.vertexlist = VertexList(item.verts, item.colors, GL_QUADS)
        self.batch.add_indexed(
            item.vertexlist.num_verts,
            item.vertexlist.primitive,
            self.groups[item.render_layer],
            item.vertexlist.indices,
            ('v2f/static', item.vertexlist.verts),
            ('c3B/static', item.vertexlist.colors) )


    def create_item_label(self, item):
        item.label = Label(
            item.text,
            font_size=item.font_size,
            x=item.x, y=item.y,
            anchor_x=item.anchor_x, anchor_y=item.anchor_y,
            batch=self.batch,
            group=self.groups[item.render_layer] )


    def add_item_to_batch(self, _, item):
        if hasattr(item, 'sprite'):
            self.create_item_sprite(item)
        elif hasattr(item, 'vertexlist'):
            self.create_item_vertexlist(item)
        elif hasattr(item, 'label'):
            self.create_item_label(item)


    def remove_item_from_batch(self, _, item):
        if hasattr(item, 'sprite'):
            item.sprite.batch = None
            item.sprite.delete()
        elif hasattr(item, 'vertexlist'):
            item.vertexlist.delete()
        elif hasattr(item, 'label'):
            item.label.delete()

