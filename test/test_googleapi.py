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

    def simulate_captcha_login(self, *args, **kwargs):
        """This method is a side effect for test_captcha_login"""
        if self.captcha_error_thrown:
            self.assertIn('captcha_token', kwargs.keys())
            self.assertIn('captcha_response', kwargs.keys())
            return None
        self.captcha_error_thrown = True
        raise gdata.service.CaptchaRequired

    @patch('gdata.calendar.service.CalendarService.ClientLogin')
    def test_login(self, mock):
        client = googleapi.Client('username@host', 'password')
        mock.assert_called_with('username@host', 'password',
                captcha_token=None, captcha_response=None,
                service="Maemo Gcal sync {0}".format(maemogcalsync.__version__))
    
    @patch('gdata.calendar.service.CalendarService.ClientLogin')
    def test_captcha_login(self, mock):
        run_once = False
        mock.side_effect = self.simulate_captcha_login
        with self.assertRaises(gdata.service.CaptchaRequired):
            googleapi.Client('username@host', 'password')
        googleapi.Client('username@host', 'password', 'captchatoken', 'captcharesponse')
        self.assertEqual(2, mock.call_count)


if __name__ == "__main__":
    unittest.main()
