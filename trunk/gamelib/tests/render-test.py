
from mock import Mock

from pyglet.image import SolidColorImagePattern

from unittestplus.testcaseplus import TestCasePlus
from unittestplus.run import run

from ..worlditem import WorldItem
from ..render import Render
from ..arena import Arena


_dummy_image = \
    SolidColorImagePattern(color=(0, 0, 0, 0)).create_image(64, 64)


class RenderTest(TestCasePlus):

    def test_AddItemToWorldAddsItToRenderBatchToo(self):
        item1, item2, item3 = WorldItem(), WorldItem(), WorldItem()
        arena = Arena(None, None)
        application = Mock()
        application.arena = arena
        render = Render(arena)
        render.images = dict(WorldItem=[_dummy_image])
        WorldItem.images = [_dummy_image]

        arena.add(item1)
        arena.add(item2)
        arena.add(item3)

        self.assertIs(item1.sprite.batch, render.batch)
        self.assertIs(item2.sprite.batch, render.batch)
        self.assertIs(item3.sprite.batch, render.batch)


    def test_RemoveItemFromWorldRemovesFromRenderBatchToo(self):
        item1, item2, item3 = WorldItem(), WorldItem(), WorldItem()
        arena = Arena(None, None)
        application = Mock()
        application.arena = arena
        render = Render(arena)
        render.images = dict(WorldItem=[_dummy_image])
        WorldItem.images = [_dummy_image]

        arena.add(item1)
        arena.add(item2)
        arena.add(item3)

        arena.remove(item2)

        self.assertIs(item1.sprite.batch, render.batch)
        self.assertNone(item2.sprite.batch)
        self.assertIs(item3.sprite.batch, render.batch)



if __name__ == '__main__':
    run(RenderTest)

