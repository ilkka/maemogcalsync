"""Google API module of maemogcalsync.

This module takes care of interfacing with the Google APIs."""
from maemogcalsync.event import Event

def get_events_since(calendar, last_sync):
    return [Event(), Event()]

def get_user_calendars():
    return ['calendar1', 'calendar2']
