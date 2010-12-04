"""Google API module of maemogcalsync.

This module takes care of interfacing with the Google APIs."""
from maemogcalsync.event import Event

def get_events_since(calendar, last_sync):
    return [Event('event1'), Event('event2')]

def get_user_calendars():
    return ['calendar1', 'calendar2']

def create_event(calendar, event):
    pass
