# -*- coding: utf-8 -*-
# Copyright (c) 2013, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

"""
ptime.py -  Precision time function made os-independent (should have been taken care of by python)
"""

from __future__ import print_function, division, absolute_import

import sys
import time as systime
START_TIME = None
time = None

def winTime():
    """Return the current time in seconds with high precision (windows version, use Manager.time() to stay platform independent)."""
    return systime.clock() + START_TIME
    #return systime.time()

def unixTime():
    """Return the current time in seconds with high precision (unix version, use Manager.time() to stay platform independent)."""
    return systime.time()

if sys.platform.startswith('win'):
    cstart = systime.clock()  ### Required to start the clock in windows
    START_TIME = systime.time() - cstart
    
    time = winTime
else:
    time = unixTime

