#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
"""
short module explanation


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
from django.middleware.csrf import CsrfViewMiddleware as OriginalCsrfViewMiddleware


class CsrfViewMiddleware(OriginalCsrfViewMiddleware):
    """
    CsrfViewMiddleware which use UID insted of cookie to store
    csrf token when the device does not support cookie

    """

    def process_response(self, request, response):
        if getattr(request.COOKIES, '_mfw_overridden', False):
            # cookie is not available thus override set_cookie method
            # of response instance.
            #
            # Note:
            #   middleware of django is called bottom up order for
            #   response phase that's why this middleware is required
            #   even mfw.middleware.session.SessionMiddleware does
            #   exactlly same thing.
            #
            if not getattr(response.set_cookie, '_mfw_overridden', False):
                def set_cookie(key, value, **kwargs):
                    request.session[key] = value
                    request.session.save()
                response.set_cookie = set_cookie
                response.set_cookie._mfw_overridden = True
        return super(CsrfViewMiddleware, self).process_response(request, response)
