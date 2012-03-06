# vim: set fileencoding=utf-8 :
"""
Encoding middleware to enable converting encoding of response to
display the response properly in device which cannot understand
standard utf-8 response.


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
from django.utils.encoding import force_unicode


def encode(src, encoding):
    c = force_unicode(src)
    # insted of raise exception, replace character which cannot encode.
    dst = c.encode(encoding, 'replace')
    return dst

class DeviceEncodingMiddleware(object):
    """Middleware for convert response encoding to encoding which detected device use."""
    def process_request(self, request):
        # tell django to use device encoding
        request.encoding = request.device.encoding

    def process_response(self, request, response):
        if request.device.encoding == settings.DEFAULT_CHARSET:
            return response

        if response['content-type'].startswith('text/') and not getattr(response, '_mfw_encoded', False):
            # encode only for text
            response.content = encode(response.content, request.device.encoding)
            response['content-type'] = 'application/xhtml+xml; charset=%s' % request.device.encoding
            response._mfw_encoded = True

        return response
