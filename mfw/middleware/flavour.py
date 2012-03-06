# vim: set fileencoding=utf-8 :
"""
Flavour middleware to enable flavour template system


AUTHOR:
    lambdalisue[Ali su ae] (lambdalisue@hashnote.net)
    
License:
    The MIT License (MIT)

    Copyright (c) 2012 Alisue allright reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to
    deal in the Software without restriction, including without limitation the
    rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
    sell copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
    IN THE SOFTWARE.

"""
from __future__ import with_statement
import os
from django.conf import settings
try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()
def get_flavour():
    """get stored flavour in threadlocal"""
    return getattr(_thread_locals, 'flavour', None)


def parse_device(device):
    """parse device and return device flavour"""

    # try to load flavour from cache because generating
    # flavour may slow.
    if device in parse_device._cache:
        return parse_device._cache[device]
    
    columns = list(settings.MFW_DEVICE_FLAVOUR_COLUMNS(device))
    for overlap_rule in settings.MFW_DEVICE_FLAVOUR_OVERLAP_RULES:
        condition, overlap = overlap_rule
        if condition(device, columns):
            columns = overlap(device, columns)
            if isinstance(columns, tuple):
                columns = list(columns)

    # remove all empty columns
    columns = filter(bool, columns)

    if columns:
        flavour = os.path.join(*columns)
    else:
        flavour = ''

    parse_device._cache[device] = flavour
    return flavour
parse_device._cache = {}


class DeviceFlavourDetectionMiddleware(object):
    """create ``flavour`` from ``request.device`` and store in ``flavour`` attribute"""
    def process_request(self, request):
        flavour = parse_device(request.device)
        request.flavour = flavour
        # store flavor in thread local
        _thread_locals.flavour = flavour
