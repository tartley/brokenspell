
from pyglet import clock
from pyglet.gl import (
    glBlendFunc, glEnable,
    GL_BLEND, GL_ONE_MINUS_SRC_ALPHA, GL_QUADS, GL_SRC_ALPHA,
)
from pyglet.graphics import Batch, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.text import Label

from gameitem import GameItem
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

        self.application.arena.item_added += self.add_item_to_batch
        self.application.arena.item_removed += self.remove_item_from_batch

        self.clockDisplay = clock.ClockDisplay()
        self.ground = None
        self.batch = Batch()


    def init(self, win):
        graphics = Graphics()
        self.images = graphics.load()

        self.score_label = Label("0",
            font_size=36, x=win.width, y=win.height,
            anchor_x='right', anchor_y='top')

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    def draw(self):
        for item in self.application.arena.items:
            if hasattr(item, 'animate'):
                item.animate(self.images)
        self.batch.draw()

        self.application.user_message.draw()
        self.application.instructions.draw()
        self.score_label.text = '%d' % self.application.game.score
        self.score_label.draw()
        self.clockDisplay.draw()


    def add_item_to_batch(self, _, item):
        if hasattr(item, 'sprite'):
            item.sprite = Sprite(
                self.images[item.__class__.__name__][0],
                batch=self.batch,
                group=self.groups[item.render_layer]
            )
            item.update_sprite_stats()
        elif hasattr(item, 'vertexlist'):
            vertexlist = VertexList(item.verts, item.colors, GL_QUADS)
            item.vertexlist = vertexlist
            self.batch.add_indexed(
                vertexlist.num_verts,
                vertexlist.primitive,
                self.groups[item.render_layer],
                vertexlist.indices,
                ('v2f/static', vertexlist.verts),
                ('c3B/static', vertexlist.colors)
            )


    def remove_item_from_batch(self, _, item):
        if hasattr(item, 'sprite'):
            item.sprite.batch = None
            item.sprite.delete()
        elif hasattr(item, 'vertexlist'):
            item.vertexlist.batch = None # speculative code
            item.vertexlist.delete()

