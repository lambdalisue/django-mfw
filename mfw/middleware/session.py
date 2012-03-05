# vim: set fileencoding=utf-8 :
"""
SessionMiddleware which use cache insted of cookie to store
session key when the device does not support cookie


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
from django.contrib.sessions.middleware import SessionMiddleware as DjangoSessionMiddleware

def get_device(request):
    from mfw.core import detect
    return getattr(request, 'device', detect(request.META))

class SessionMiddleware(DjangoSessionMiddleware):
    def process_request(self, request):
        device = get_device(request)

        if device.support_cookie:
            super(SessionMiddleware, self).process_request(request)
            return

        # DoCoMo doesn't return uid request in GET without `guid=on` thus redirect
        if device.carrier == 'docomo' and request.method == 'GET' and not request.GET.has_key('guid'):
            protocol = 'https' if request.is_secure() else 'http'
            query_string = '&guid=on' if request.GET else '?guid=on'
            url = "%s://%s%s%s" % (
                    protocol,
                    request.get_host(),
                    request.get_full_path(),
                    query_string
                )
            return redirect(url)

        if device.uid:
            # get session_key from cache
            session_key = cache.get(
                    settings.SESSION_COOKIE_NAME + '_%s_%s' % (
                        device.carrier, device.uid
                    ))
        else:
            session_key = None
        
        # create session instance via session_key
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore(session_key)


    def process_response(self, request, response):
        device = get_device(request)
        
        if not device.support_cookie:
            def set_cookie(key, value, max_age=None, 
                    expires=None, path='/', domain=None,
                    secure=False, httponly=False):
                cache.set(
                        key + "_%s_%s" % (device.carrier, device.uid),
                        value, max_age)
            response.set_cookie = set_cookie
        return super(SessionMiddleware, self).process_response(request, response)
