
from mock import Mock
from unittestplus.testcaseplus import TestCasePlus
from unittestplus.run import run

import fixpath

from sinisterducks.event import Event


class EventTest(TestCasePlus):

    def test_ZeroListeners(self):
        event = Event()
        event()

    def test_ListenersGetCalled(self):
        event = Event()
        mock1 = Mock()
        mock2 = Mock()
        event += mock1
        event += mock2

        event()

        self.assertTrue(mock1.called)
        self.assertTrue(mock2.called)


    def test_AddingListenerTwiceRaises(self):
        event = Event()
        mock = Mock()

        def add(event, mock):
            event += mock

        add(event, mock)
        expected_msg = 'msg'
        #'listener already subscribed to event\n  %s\n  %s' \
        #    % (mock, event)
        self.assertRaises(lambda: add(event, mock), KeyError, expected_msg)


    def test_ListenersCanBeRemoved(self):
        event = Event()
        mock1 = Mock()
        mock2 = Mock()
        event += mock1
        event += mock2

        event -= mock1

        event()

        self.assertFalse(mock1.called)
        self.assertTrue(mock2.called)


    def test_RemovingNonListenersRaises(self):
        event = Event()
        nonlistener = object()

        def remove(event, nonlistener):
            event -= nonlistener

        expected_msg = 'listener not subscribed to this event:\n  %s\n  %s' \
            % (nonlistener, event)
        self.assertRaises(
            lambda: remove(event, nonlistener),
            KeyError, expected_msg)


    def test_RemovingListenersMultipleTimesRaises(self):
        mock = Mock()
        event = Event()
        event += mock

        def remove(event, mock):
            event -= mock

        remove(event, mock)
        expected_msg = 'listener not subscribed to this event:\n  %s\n  %s' \
            % (mock, event)
        self.assertRaises(lambda: remove(event, mock), KeyError, expected_msg)


    def test_str(self):
        self.assertEquals(str(Event()), 'Event')

        class MyEvent(Event): pass
        self.assertEquals(str(MyEvent()), 'MyEvent')



if __name__ == '__main__':
    run(EventTest)

