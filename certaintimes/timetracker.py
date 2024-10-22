"""Track elapsed time."""
# Copyright (c) Microsoft Corporation. All rights reserved.
# Highly Confidential Material
import time


class TimeTracker:
    """Elapsed time tracker."""

    def __init__(self):
        """Initialise."""
        self._start_time = time.time()

    @property
    def elapsed_hms(self):
        """
        Elapsed time as HH:MM:SS.

        :return: elapsed time as string
        """
        event_time = time.time()
        elapsed_secs = int(event_time - self._start_time)
        return hms(elapsed_secs)

    def start(self):
        """Set start time."""
        self._start_time = time.time()


def hms(seconds):
    """
    Return time as string in format HH:MM:SS.

    :param seconds: seconds as integer
    :return: time as HH:MM:SS string
    """
    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    secs = seconds % 60
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, secs)
