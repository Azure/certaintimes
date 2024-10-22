#!/usr/bin/env python
"""Log certain times of interest."""
# Copyright (c) Microsoft Corporation. All rights reserved.
# Highly Confidential Material
import argparse
import logging
import logging.config
import logging.handlers
import sys
import time
from datetime import datetime, timezone

from certaintimes.timetracker import TimeTracker, hms

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.NullHandler())


class UTCFormatter(logging.Formatter):
    """UTC formatter."""

    converter = time.gmtime


def main():
    """Run."""
    # Parse options and sort out logging
    parser = argparse.ArgumentParser(prog="certaintimes")
    parser.add_argument("-o", "--observer", help="optional observer name")
    args = parser.parse_args()
    if args.observer:
        prefix = "{}: ".format(args.observer)
        logfile = "certaintimes-{}.log".format(args.observer)
    else:
        prefix = ""
        logfile = "certaintimes.log"
    print(
        "Enter text to append it as a UTC timed log entry to {}, q or quit to exit.\n".format(
            logfile
        )
    )
    print(
        "local time: {}\n       UTC: {}\n".format(
            datetime.now(), datetime.now(timezone.utc)
        )
    )
    print(
        "IMPORTANT: WSL can get out of sync over sleep!\n"
        "If this time does not look close, please exit and fix e.g. with 'sudo hwclock -s'"
    )

    setuplogging(logfile)

    LOG.info("%s%s ====== Starting session ======", prefix, hms(0))
    tracker = TimeTracker()

    while True:
        line = sys.stdin.readline().rstrip()
        elapsed = tracker.elapsed_hms
        if line in ["quit", "q"]:
            LOG.info("%s%s ====== Ending session ======", prefix, elapsed)
            break
        print("{} {}".format(elapsed, line))
        LOG.info("%s%s %s", prefix, elapsed, line)
    logging.shutdown()


def setuplogging(logfile):
    """
    Set up logging with UTC millisecond timestamps.

    :param logfile: optional observer name
    """
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "detail": {
                    "()": UTCFormatter,
                    "format": ("%(asctime)s.%(msecs)03dZ %(message)s"),
                    "datefmt": "%Y-%m-%dT%H:%M:%S",
                },
            },
            "handlers": {
                "timedsession": {
                    "class": "logging.FileHandler",
                    "filename": logfile,
                    "formatter": "detail",
                },
            },
            "loggers": {
                "": {"handlers": ["timedsession"], "level": "INFO"},
            },
        }
    )


if __name__ == "__main__":
    main()
