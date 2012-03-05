# vim: set fileencoding=utf-8 :
"""
CsrfViewMiddleware which use session insted of cookie
when the device does not support cookie. To enable session based csrf protection,
you must use CacheBasedSessionMiddleware as well.


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
from django.middleware.csrf import CsrfViewMiddleware


class SessionBasedCsrfViewMiddleware(CsrfViewMiddleware):
    """
    CsrfViewMiddleware which use session insted of cookie
    when the device does not support cookie.

    """
    def process_view(self, request, *args, **kwargs):
        if not request.device.support_cookie:
            # the device does not support cookie so use session insted
            request.COOKIES = request.session
        return super(SessionBasedCsrfViewMiddleware, self).process_view(request, *args, **kwargs)

    def process_response(self, request, response):
        if not request.device.support_cookie:
            # the device does not support cookie so override set_cookie method
            # to use session insted of cookie
            response.csrf_processing_done = False
            def set_cookie(key, value, max_age=None, 
                    expires=None, path='/', domain=None,
                    secure=False, httponly=False):
                request.session[key] = value
                request.session.save()
            response.set_cookie = set_cookie
        return super(SessionBasedCsrfViewMiddleware, self).process_response(request, response)

