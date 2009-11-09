
from mock import Mock

from unittestplus.testcaseplus import TestCasePlus
from unittestplus.run import run

from gamelib.gameent import WorldItem
from gamelib.render import Render
from gamelib.world import World


class RenderTest(TestCasePlus):

    def test_AddItemToWorldAddsItToRenderBatchToo(self):
        item1, item2, item3 = WorldItem(), WorldItem(), WorldItem()
        world = World(None, None, None)
        application = Mock()
        application.world = world
        render = Render(application, None)

        world.add(item1)
        world.add(item2)
        world.add(item3)

        self.assertIs(item1.sprite.batch, render.batch)
        self.assertIs(item2.sprite.batch, render.batch)
        self.assertIs(item3.sprite.batch, render.batch)


    def test_RemoveItemFromWorldRemovesFromRenderBatchToo(self):
        item1, item2, item3 = WorldItem(), WorldItem(), WorldItem()
        world = World(None, None, None)
        application = Mock()
        application.world = world
        render = Render(application, None)

        world.add(item1)
        world.add(item2)
        world.add(item3)

        world.remove(item2)

        self.assertIs(item1.sprite.batch, render.batch)
        self.assertNone(item2.sprite.batch)
        self.assertIs(item3.sprite.batch, render.batch)



if __name__ == '__main__':
    run(RenderTest)

