
from mock import Mock
from unittestplus.testcaseplus import TestCasePlus
from unittestplus.run import run

import fixpath

from sinisterducks.event import Event
from sinisterducks.gameitem import GameItem
from sinisterducks.render import Render
from sinisterducks.worlditem import WorldItem


class RenderTest(TestCasePlus):

    def test_on_add_item(self):
        game = Mock()
        game.item_added = Event()
        game.item_removed = Event()
        render = Render(game)
        item = GameItem()

        render.on_add_item(item)
        # item.add_to_batch doesn't exist and is not called

        item.add_to_batch = Mock()
        render.on_add_item(item)
        self.assertEquals(
            item.add_to_batch.call_args,
            ((render.batch, render.groups), {})
        )


    def test_on_remove_item(self):
        game = Mock()
        game.item_added = Event()
        game.item_removed = Event()
        render = Render(game)
        item = GameItem()

        render.on_remove_item(item)
        # item.remove_from_batch doesn't exist and is not called

        item.remove_from_batch = Mock()
        render.on_remove_item(item)
        self.assertEquals(
            item.remove_from_batch.call_args,
            ((render.batch, ), {})
        )


if __name__ == '__main__':
    run(RenderTest)

