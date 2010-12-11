"""Unit test suite for the Google API part."""
import unittest2 as unittest
from datetime import datetime, timedelta
import random
import logging
import gdata.calendar
import gdata.calendar.service
import yaml
import os.path
from mock import Mock, patch


Alphabet = 'abcdefghijlkmnopqrstuvwxyz0123456789'


from maemogcalsync import googleapi
from maemogcalsync.event import Event


Log = logging.getLogger('test.googleapi')


class TestGoogleApi(unittest.TestCase):
    """Test suite class for googleapi module."""

    @patch('gdata.calendar.service.CalendarService.ClientLogin')
    def test_login(self, mock):
        client = googleapi.Client('username@host', 'password')
        mock.assert_called_with('username@host', 'password', service='Maemo Gcal sync 0.1')
    

if __name__ == "__main__":
    unittest.main()
