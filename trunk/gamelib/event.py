
class Event(object):

    def __init__(self, listener=None):
        self.listeners = set()
        if listener:
            self += listener


    def __iadd__(self, listener):
        if listener not in self.listeners:
            self.listeners.add(listener)
        else:
            msg = 'listener already subscribed to event\n  %s\n  %s' \
                % (listener, self)
            raise KeyError('msg')
        return self


    def __isub__(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)
        else:
            msg = 'listener not subscribed to this event:\n  %s\n  %s' \
                % (listener, self)
            raise KeyError(msg)
        return self


    def __call__(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)


    def __str__(self):
        return self.__class__.__name__

