# Copyright (c) Microsoft Corporation. All rights reserved.
# Highly Confidential Material
"""Certain times."""
from pkg_resources import DistributionNotFound, get_distribution

# Try and expose __version__, as per PEP396.
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
