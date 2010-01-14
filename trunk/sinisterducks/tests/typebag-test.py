
from mock import Mock
from unittestplus.testcaseplus import TestCasePlus
from unittestplus.run import run

import fixpath

from sinisterducks.typebag import TypeBag


class TypeBagTest(TestCasePlus):

    def test_init(self):
        bag = TypeBag()
        self.assertEquals(bag.items, {})


    def test_add(self):
        bag = TypeBag()

        o1 = 123
        bag.add(o1)
        self.assertEquals(bag.items, {id(o1): o1})
        self.assertEquals(bag.by_type, {int: set([id(o1)])})

        o2 = 456
        bag.add(o2)
        self.assertEquals(bag.items, {id(o1): o1, id(o2): o2})
        self.assertEquals(bag.by_type, { int: set([id(o1), id(o2)]), })

        o3 = [789]
        bag.add(o3)
        self.assertEquals(bag.items, {id(o1): o1, id(o2): o2, id(o3): o3})
        self.assertEquals(bag.by_type, {
            int: set([id(o1), id(o2)]),
            list: set([id(o3)]),
        })


    def create_populated_bag(self):
        bag = TypeBag()
        o1 = 123
        o2 = 456
        o3 = [789]
        bag.add(o1)
        bag.add(o2)
        bag.add(o3)
        return bag, [o1, o2, o3]


    def test_add_same_thing_fails(self):
        bag = TypeBag()
        o1 = 123
        bag.add(o1)
        self.assertRaises(lambda: bag.add(o1), ValueError)


    def test_remove(self):
        bag, (o1, o2, o3) = self.create_populated_bag()

        bag.remove(o3)
        self.assertEquals(bag.items, {id(o1): o1, id(o2): o2})
        self.assertEquals(bag.by_type, { int: set([id(o1), id(o2)]), })

        bag.remove(o2)
        self.assertEquals(bag.items, {id(o1): o1})
        self.assertEquals(bag.by_type, {int: set([id(o1)])})

        bag.remove(o1)
        self.assertEquals(bag.items, {})
        self.assertEquals(bag.by_type, {})


    def test_remove_by_id(self):
        bag, (o1, o2, o3) = self.create_populated_bag()

        bag.remove(itemid=id(o3))
        self.assertEquals(bag.items, {id(o1): o1, id(o2): o2})
        self.assertEquals(bag.by_type, { int: set([id(o1), id(o2)]), })

        bag.remove(itemid=id(o2))
        self.assertEquals(bag.items, {id(o1): o1})
        self.assertEquals(bag.by_type, {int: set([id(o1)])})

        bag.remove(itemid=id(o1))
        self.assertEquals(bag.items, {})
        self.assertEquals(bag.by_type, {})


    def test_remove_takes_item_xor_id(self):
        bag = TypeBag()
        self.assertRaises(bag.remove, AssertionError)
        self.assertRaises(
            lambda: bag.remove(item=123, itemid=456),
            AssertionError)


    def test_remove_item_that_isnt_in_the_bag(self):
        bag = TypeBag()
        o1 = 123
        bag.add(o1)
        self.assertRaises(lambda: bag.remove(456), KeyError)
        self.assertRaises(lambda: bag.remove(7.89), KeyError)
        bag.remove(o1)
        self.assertRaises(lambda: bag.remove(o1), KeyError)


    def test_remove_returns_the_removed_item(self):
        bag = TypeBag()
        o1 = 123
        bag.add(o1)
        self.assertIs(bag.remove(itemid=id(o1)), o1)


    def test_iterate_over_all_items(self):
        bag, (o1, o2, o3) = self.create_populated_bag()

        expected = [o1, o2, o3]
        for item in bag:
            expected.remove(item)
        self.assertEquals(expected, [])


    def test_simultaneous_iterations_by_type(self):
        bag, (o1, o2, o3) = self.create_populated_bag()

        expected1 = [o1, o2]
        for item1 in bag[int]:
            expected1.remove(item1)
            expected2 = [o1, o2]
            for item2 in bag[int]:
                expected2.remove(item2)
        self.assertEquals(expected1, [])
        self.assertEquals(expected2, [])


    def test_index_by_type(self):
        bag, (o1, o2, o3) = self.create_populated_bag()

        expected = [o1, o2]
        for item in bag[int]:
            expected.remove(item)
        self.assertEquals(expected, [])


if __name__ == '__main__':
    run(TypeBagTest)

