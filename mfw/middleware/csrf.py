# vim: set fileencoding=utf-8 :
"""
CsrfViewMiddleware which use session insted of cookie
when the device does not support cookie.


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
from django.middleware.csrf import CsrfViewMiddleware as DjangoCsrfViewMiddleware

def get_device(request):
    from mfw.core import detect
    return getattr(request, 'device', detect(request.META))

class CsrfViewMiddleware(DjangoCsrfViewMiddleware):
    def process_view(self, request, *args, **kwargs):
        device = get_device(request)
        if not device.support_cookie:
            request.COOKIES = request.session
        response = super(CsrfViewMiddleware, self).process_view(request, *args, **kwargs)
        return response

    def process_response(self, request, response):
        device = get_device(request)
        if not device.support_cookie:
            response.csrf_processing_done = False
            def set_cookie(key, value, max_age=None, 
                    expires=None, path='/', domain=None,
                    secure=False, httponly=False):
                request.session[key] = value
                request.session.save()
            response.set_cookie = set_cookie
        return super(CsrfViewMiddleware, self).process_response(request, response)

