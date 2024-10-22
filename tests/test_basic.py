# Copyright (c) Microsoft Corporation. All rights reserved.
# Highly Confidential Material
"""Basic tests."""
import unittest

from certaintimes.timetracker import hms


class TestBasic(unittest.TestCase):
    """Basic tests."""

    def test_hms(self):
        """Test hms formatting."""
        self.assertEqual(hms(0), "00:00:00")
        self.assertEqual(hms(62), "00:01:02")
        self.assertEqual(hms(3663), "01:01:03")
        self.assertEqual(hms(100 * 3600), "100:00:00")


if __name__ == "__main__":
    unittest.main()
