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
    cookie = 'support_cookie' if device.support_cookie else 'unsupport_cookie'
    kind = device.kind or ''
    name = device.name or ''
    model = device.model or ''
    version = device.version or ''

    kwargs = {
            'cookie': cookie.lower(),
            'kind': kind.lower(),
            'name': name.lower(),
            'model': model.lower(),
            'version': version.lower(),
        }                                     
    key = hash(frozenset(kwargs.items()))
    if key in parse_device._cache:
        return parse_device._cache[key]
    
    flavour = settings.MFW_FLAVOUR_PATTERN % kwargs
    flavour = flavour.replace('////', '/')
    flavour = flavour.replace('///', '/')
    flavour = flavour.replace('//', '/')
    if flavour.startswith('/'):
        flavour = flavour[1:]
    if flavour.endswith('/'):
        flavour = flavour[:-1]

    parse_device._cache[key] = flavour
    return flavour
parse_device._cache = {}


class DeviceFlavourDetectionMiddleware(object):
    """create ``flavour`` from ``request.device`` and store in ``flavour`` attribute"""
    def process_request(self, request):
        flavour = parse_device(request.device)
        request.flavour = flavour
        # store flavor in thread local
        _thread_locals.flavour = flavour
