"""Unit test suite for the Google API part."""
import unittest2 as unittest
from datetime import datetime, timedelta
import random
import logging
import gdata.calendar
import gdata.calendar.service
import yaml
import os.path


Alphabet = 'abcdefghijlkmnopqrstuvwxyz0123456789'


from maemogcalsync import googleapi
from maemogcalsync.event import Event


Log = logging.getLogger('test.googleapi')


class TestGoogleApi(unittest.TestCase):
    """Test suite class for googleapi module.
    
    Reads login credentials for the Google API from a file named
    'test_credentials.yaml' in the project root dir. This file must exist."""

    def setUp(self):
        cred_file_path = os.path.realpath(
                os.path.join(os.path.dirname(__file__),
                             '..', 'test_credentials.yaml'))
        self.assertTrue(os.path.isfile(cred_file_path),
                "Credentials file {0} must exist".format(cred_file_path))
        cred_file = open(cred_file_path, 'r')
        self.credentials = yaml.load(cred_file)
        cred_file.close()

        self.assertIsNotNone(self.credentials['username'])
        self.assertIsNotNone(self.credentials['password'])

        Log.info("Logging in to service")
        self.cal_service = gdata.calendar.service.CalendarService()
        self.cal_service.email = self.credentials['username']
        self.cal_service.password = self.credentials['password']
        self.cal_service.source = 'Maemo_Gcal_Sync-0.1' # FIXME
        self.cal_service.ProgrammaticLogin()

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
