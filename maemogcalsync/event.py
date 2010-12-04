"""Event module.

Defines the Event class."""

from enum import Enum

class Event(object):
    Visibility = Enum('Public', 'Private')

    def __init__(self, title, description = None, **kwargs):
        self._title = title
        self._description = description
