# vim: set fileencoding=utf-8 :
"""
SessionMiddleware which use UID insted of cookie to store
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
import re
import uuid
from django.conf import settings
from django.shortcuts import redirect
from django.utils.importlib import import_module
from django.contrib.sessions.middleware import SessionMiddleware as OriginalSessionMiddleware
from django.contrib.sessions.backends.base import CreateError


def create_session_key(carrier, uid):
    """create session key with carrier and uid"""
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, carrier+uid))

class SessionMiddleware(OriginalSessionMiddleware):
    """
    SessionMiddleware which use UID insted of cookie to store
    session key when the device does not support cookie

    """
    def process_request(self, request):
        if request.device.support_cookie or not hasattr(request.device, 'uid'):
            # do not use this middleware for device which support cookie or
            # doesn't have uid
            return super(SessionMiddleware, self).process_request(request)

        if not settings.MFW_SESSION_TRUST_NON_RELIABLE_DEVICE and not request.device.reliable:
            # the device cannot be trusted so do not use cache based session
            return super(SessionMiddleware, self).process_request(request)


        if request.device.uid:
            # get session_key from cache
            session_key = create_session_key(request.device.carrier, request.device.uid)
        else:
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
            session_key = None
        
        # create session instance via session_key
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore(session_key)
        # `_get_new_session_key` rewrite session key thus
        # override the method otherwise session key for
        # particular user will be losted.
        request.session._get_new_session_key = lambda : session_key
        def create(self):
            # _get_new_session_key return same value thus simply
            # over write the existing session data.
            self.session_key = self._get_new_session_key()
            try:
                self.save(must_create=True)
            except CreateError:
                self.save()
            self.modified = True
            self._session_cache = {}
            return
        request.session.__class__.create = create

        # cookie is not available in this device thus override the
        # COOKIES attribute with session instance
        request.COOKIES = request.session
        request.COOKIES._mfw_overridden = True

        return None


    def process_response(self, request, response):
        if getattr(request.COOKIES, '_mfw_overridden', False):
            # cookie is not available thus override set_cookie method
            # of response instance.
            if not getattr(response.set_cookie, '_mfw_overridden', False):
                def set_cookie(key, value, **kwargs):
                    request.session[key] = value
                    request.session.save()
                response.set_cookie = set_cookie
                response.set_cookie._mfw_overridden = True
            if request.device.carrier == 'docomo':
                # Add guid=on to all internal links found in response for
                # handling docomo
                url_pattern = re.compile(r"""((?:action|href)=["'])(?P<url>[^"']*)(["'])""")
                def repl(m):
                    url = m.group('url')
                    if url.startswith('http') or 'guid=on' in url:
                        # non internal link or already has
                        return m.group(0)
                    if '?' not in url:
                        url = url + '?guid=on'
                        return m.expand(r"\1%s\3" % url)
                    else:
                        url = url + '&guid=on'
                        return m.expand(r"\1%s\3" % url)
                response.content = url_pattern.sub(repl, response.content)
        return super(SessionMiddleware, self).process_response(request, response)
