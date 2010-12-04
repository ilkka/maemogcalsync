"""Unit test suite for the Google API part."""
import unittest2 as unittest
from datetime import datetime, timedelta
import random
import logging
import gdata.calendar
import yaml


Alphabet = 'abcdefghijlkmnopqrstuvwxyz0123456789'


from maemogcalsync import googleapi
from maemogcalsync.event import Event


Log = logging.getLogger('test.googleapi')


class TestGoogleApi(unittest.TestCase):
    """Test suite class"""

    def setUp(self):
        self.calname = reduce(lambda x, y: x + y,
                              random.sample(Alphabet, 10),
                              "")
        Log.info("Creating test calendar \"{0}\"".format(self.calname))
        cal = gdata.calendar.CalendarListEntry()

    def tearDown(self):
        Log.info("Deleting test calendar \"{0}\"".format(self.calname))

    def test_get_user_calendars(self):
        """Test fetching users's calendars."""
        calendars = googleapi.get_user_calendars()
        self.assertGreater(len(calendars), 0)

    def test_get_new_events(self):
        """Test fetching new events.

        Fetches last 20 days of events. Probably has trouble if no events
        exist within the last 20 days."""
        lastsync = datetime.utcnow() - timedelta(days = 20)
        calendars = googleapi.get_user_calendars()
        events = googleapi.get_events_since(calendars[0], lastsync)
        self.assertGreater(len(events), 0)
        self.assertIsInstance(events[0], Event)

    def test_create_event(self):
        """Test creating a new event."""
        dt_begin = datetime.utcnow() + timedelta(days = 10 * 365)
        dt_end = datetime.utcnow() + timedelta(days = 10 * 365, hours = 3)
        dt_before = dt_begin - timedelta(days = 1)
        calendars = googleapi.get_user_calendars()
        events_before = googleapi.get_events_since(calendars[0], dt_before)
        ev = Event('Test event', begin = dt_begin, end = dt_end,
                   visibility = Event.Visibility.Private)
        googleapi.create_event(calendars[0], ev)
        events = googleapi.get_events_since(calendars[0], dt_before)
        self.assertGreater(len(events), len(events_before))


if __name__ == "__main__":
    unittest.main()
