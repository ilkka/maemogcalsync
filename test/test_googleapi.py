"""Unit test suite for the Google API part."""
import unittest2 as unittest
from datetime import datetime, timedelta

from maemogcalsync import googleapi
from maemogcalsync.event import Event

class TestGoogleApi(unittest.TestCase):
    """Test suite class"""
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
        ev = Event('Test event',
                   begin = datetime.utcnow() + timedelta(days = 10 * 365),
                   end = datetime.utcnow() + timedelta(days = 10 * 365,
                                                       hours = 3),
                   visibility = Event.Visibility.Private)
        calendars = googleapi.get_user_calendars()
        googleapi.create_event(calendars[0], ev)


if __name__ == "__main__":
    unittest.main()
