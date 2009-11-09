
from mock import Mock

from unittestplus.testcaseplus import TestCasePlus
from unittestplus.run import run

from gamelib.gameent import GameEnt
from gamelib.render import Render
from gamelib.world import World


class RenderTest(TestCasePlus):

    def test_AddEntityToWorldAddsItToRenderBatchToo(self):
        ent1, ent2, ent3 = GameEnt(), GameEnt(), GameEnt()
        world = World(None, None, None)
        application = Mock()
        application.world = world
        render = Render(application, None)

        world.add(ent1)
        world.add(ent2)
        world.add(ent3)

        self.assertIs(ent1.sprite.batch, render.batch)
        self.assertIs(ent2.sprite.batch, render.batch)
        self.assertIs(ent3.sprite.batch, render.batch)


    def test_RemoveEntityFromWorldRemovesFromRenderBatchToo(self):
        ent1, ent2, ent3 = GameEnt(), GameEnt(), GameEnt()
        world = World(None, None, None)
        application = Mock()
        application.world = world
        render = Render(application, None)

        world.add(ent1)
        world.add(ent2)
        world.add(ent3)

        world.remove(ent2)

        self.assertIs(ent1.sprite.batch, render.batch)
        self.assertNone(ent2.sprite.batch)
        self.assertIs(ent3.sprite.batch, render.batch)



if __name__ == '__main__':
    run(RenderTest)

