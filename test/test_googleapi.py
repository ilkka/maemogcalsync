"""Unit test suite for the Google API part."""
import unittest2 as unittest
from datetime import datetime, timedelta

from maemogcalsync import googleapi

class TestGoogleApi(unittest.TestCase):
    """Test suite class"""
    def test_get_new_events(self):
        """Test fetching new events.

        Fetches last 20 days of events. Probably has trouble if no events
        exist within the last 20 days."""
        lastsync = datetime.utcnow() - timedelta(days=20)
        events = googleapi.get_events_since(lastsync)
        self.assertGreater(len(events), 0)


if __name__ == "__main__":
    unittest.main()
