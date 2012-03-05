# vim: set fileencoding=utf-8 :
"""
SessionMiddleware which use cache insted of cookie to store
session key when the device does not support cookie


.. Note::
    To use Cache based session, you must configure django cache system
    properly. Add required cache middlewares listed in Django documentation.


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
from django.core.cache import cache
from django.shortcuts import redirect
from django.utils.importlib import import_module
from django.contrib.sessions.middleware import SessionMiddleware


class CacheBasedSessionMiddleware(SessionMiddleware):
    """
    SessionMiddleware which use cache insted of cookie to store
    session key when the device does not support cookie

    """
    def get_session_key_name(self, request):
        pattern = settings.SESSION_COOKIE_NAME + "_%s_%s"
        return pattern % (request.device.carrier, request.device.uid)

    def process_request(self, request):
        if request.device.support_cookie or not hasattr(request.device, 'uid'):
            super(CacheBasedSessionMiddleware, self).process_request(request)
            return

        if settings.MFW_IGNORE_NON_RELIBLE_MOBILE and not request.device.reliable:
            # the device cannot be trusted so do not use cache based session
            super(CacheBasedSessionMiddleware, self).process_request(request)
            return

        # DoCoMo doesn't return uid request in GET without `guid=on` thus redirect
        if request.device.carrier == 'docomo' and request.method == 'GET' and not request.GET.has_key('guid'):
            protocol = 'https' if request.is_secure() else 'http'
            query_string = '&guid=on' if request.GET else '?guid=on'
            url = "%s://%s%s%s" % (
                    protocol,
                    request.get_host(),
                    request.get_full_path(),
                    query_string
                )
            return redirect(url)

        if request.device.uid:
            # get session_key from cache
            session_key = cache.get(self.get_session_key_name(request))
        else:
            session_key = None
        
        # create session instance via session_key
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore(session_key)


    def process_response(self, request, response):
        if not request.device.support_cookie and hasattr(request.device, 'uid'):
            # override set_cookie method to use cache insted of cookie
            def set_cookie(key, value, max_age=None, 
                    expires=None, path='/', domain=None,
                    secure=False, httponly=False):
                cache.set(self.get_session_key_name(request), value, max_age)
            response.set_cookie = set_cookie
        return super(CacheBasedSessionMiddleware, self).process_response(request, response)
