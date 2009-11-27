
class TypeBag(object):
    '''
    Maintains a collection of mutable items, in a dict, keyed by their id.
    Provides access to iterate over all items, or all items of a particular
    type.
    '''
    def __init__(self):
        # all items in the bag, keyed by id
        self.items = {}
        # key by type, value is set of item ids
        self.by_type = {}


    def add(self, item):
        ''' add an item to the bag '''
        if id(item) in self.items:
            raise ValueError('%r already in the bag' % (item,))
        self.items[id(item)] = item

        if type(item) not in self.by_type:
            self.by_type[type(item)] = set()
        self.by_type[type(item)].add(id(item))


    def remove(self, item=None, itemid=None):
        '''
        Remove an item from the bag.
        Item may either be specified directly, or by id.
        '''
        assert (item is None) ^ (itemid is None)
        if item is None:
            item = self.items[itemid]
        else:
            itemid = id(item)

        del self.items[itemid]

        itemtype = type(item)
        self.by_type[itemtype].remove(itemid)
        if len(self.by_type[itemtype]) == 0:
            del self.by_type[itemtype]

        return item


    def __iter__(self):
        ''' iterate over all items in the bag '''
        return self.items.itervalues()


    def __getitem__(self, typee):
        ''' get an iterator over all items of the given type '''
        ids = self.by_type.get(typee, set())
        return (self.items[id] for id in ids)

