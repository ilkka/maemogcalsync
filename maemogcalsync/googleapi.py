"""Google API module of maemogcalsync.

This module takes care of interfacing with the Google APIs."""
import maemogcalsync
from maemogcalsync.event import Event
import gdata.calendar.service
import gdata.service


class Client(object):
    def __init__(self, username, password):
        self.service = gdata.calendar.service.CalendarService()
        try:
            self.service.ClientLogin(username, password,
                    service="Maemo Gcal sync {0}".format(maemogcalsync.__version__))
        except gdata.service.CaptchaRequired:
            print("Visit {0} and enter the response here".format(self.service.captcha_url))
            self.service.ClientLogin(username, password,
                    service="Maemo Gcal sync {0}".format(maemogcalsync.__version__),
                    captcha_token='testcaptcha',
                    captcha_response='testresponse')


def get_events_since(calendar, last_sync):
    return [Event('event1'), Event('event2')]

def get_user_calendars():
    return ['calendar1', 'calendar2']

def create_event(calendar, event):
    pass
