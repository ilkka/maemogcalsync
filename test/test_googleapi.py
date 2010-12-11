"""Unit test suite for the Google API part."""
import unittest2 as unittest
from datetime import datetime, timedelta
import random
import logging
import gdata.service
import gdata.calendar
import gdata.calendar.service
import yaml
import os.path
from mock import Mock, patch


Alphabet = 'abcdefghijlkmnopqrstuvwxyz0123456789'


import maemogcalsync
from maemogcalsync import googleapi
from maemogcalsync.event import Event


Log = logging.getLogger('test.googleapi')


class TestGoogleApi(unittest.TestCase):
    """Test suite class for googleapi module."""

    def setUp(self):
        """Set up fixture"""
        self.captcha_error_thrown = False

    def simulate_captcha_login(self, username, password, **kwargs):
        """This method is a side effect for test_captcha_login"""
        if self.captcha_error_thrown:
            return None
        self.captcha_error_thrown = True
        raise gdata.service.CaptchaRequired

    @patch('gdata.calendar.service.CalendarService.ClientLogin')
    def test_login(self, mock):
        client = googleapi.Client('username@host', 'password')
        mock.assert_called_with('username@host', 'password', service="Maemo Gcal sync {0}".format(maemogcalsync.__version__))
    
    @patch('gdata.calendar.service.CalendarService.ClientLogin')
    def test_captcha_login(self, mock):
        run_once = False
        mock.side_effect = self.simulate_captcha_login
        client = googleapi.Client('username@host', 'password')


if __name__ == "__main__":
    unittest.main()
