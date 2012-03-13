# vim: set fileencoding=utf-8 :
"""
Middleware for detecting device


.. Note::
    This middleware must be called earlier than other MFW middlewares.


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
from mfw.device import detect


class RequestDeviceDetectionMiddleware(object):
    """detect device and add ``device`` argument to ``request`` instance"""
    def process_request(self, request):
        device = detect(request.META)
        request.device = device
        return None

class ResponseDeviceDetectionMiddleware(object):
    """detect device and add ``device`` argument to ``request`` instance"""
    def process_response(self, request, response):
        device = detect(request.META)
        request.device = device
        return response

class DeviceDetectionMiddleware(RequestDeviceDetectionMiddleware):
    """detect device and add ``device`` argument to ``request`` instance"""
    def __init__(self):
        import warnings
        warnings.warn(
                "This middleware has deprecated. Use ``RequestDeviceDetectionMiddleware`` "
                "and ``ResponseDeviceDetectionMiddleware`` insted.", DeprecationWarning
            )
        super(DeviceDetectionMiddleware, self).__init__()
