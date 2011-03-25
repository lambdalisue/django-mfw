#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/24
#
from django.shortcuts import redirect
from django.core.cache import cache
from django.utils.http import cookie_date
from django.utils.cache import patch_vary_headers
from django.utils.importlib import import_module
from django.contrib.sessions.middleware import SessionMiddleware as _SessionMiddleware

import time

from ..conf import settings
from ..core import detect

def _get_device(request):
    device = getattr(request, 'device', detect(request.META))
    return device

class SessionMiddleware(_SessionMiddleware):
    u"""Session middleware which using UID for device which doesn't support cookie."""
    _cache_key_name = 'session_key_%s'
    
    def process_request(self, request):
        device = _get_device(request)
        
        if device.support_cookie:
            super(SessionMiddleware, self).process_request(request)
            return
        else:
            # start uid based session
            engine = import_module(settings.SESSION_ENGINE)
            # DoCoMo doesn't return uid without `guid=on`
            if device.carrier == 'docomo' and request.method == 'GET' and not request.GET.has_key('guid'):
                # redirect to `guid=on`
                if request.is_secure():
                    # i-MODE ID doesn't work on SSL
                    protocol = 'https'
                else:
                    protocol = 'http'
                if request.GET:
                    query_string = '&guid=on'
                else:
                    query_string = '?guid=on'
                url = "%s://%s%s%s" % (protocol, request.get_host(), request.get_full_path(), query_string)
                return redirect(url)
            if device.uid:
                # get sessino_key from cache
                session_key = cache.get(self._cache_key_name % device.uid)
            else:
                session_key = None
        request.session = engine.SessionStore(session_key)
    
    def process_response(self, request, response):
        device = _get_device(request)
        try:
            accessed = request.session.accessed
            #modified = request.session.modified
        except AttributeError:
            pass
        else:
            if accessed:
                patch_vary_headers(response, ('Cookie',))
            #if modified or settings.SESSION_SAVE_EVERY_REQUEST:
            if request.session.get_expire_at_browser_close():
                max_age = None
                expires = None
            else:
                max_age = request.session.get_expiry_age()
                expires_time = time.time() + max_age
                expires = cookie_date(expires_time)
            # Save the session data and refresh the client cookie.
            request.session.save()
            if device.support_cookie:
                response.set_cookie(settings.SESSION_COOKIE_NAME,
                        request.session.session_key, max_age=max_age,
                        expires=expires, domain=settings.SESSION_COOKIE_DOMAIN,
                        path=settings.SESSION_COOKIE_PATH,
                        secure=settings.SESSION_COOKIE_SECURE or None)
            else:
                # Ignore device which is detected as 'spoof device' in deployment
                if device.uid and (not device.spoof or settings.DEBUG):
                    # store session_key on cache
                    cache.set(self._cache_key_name % device.uid,
                              request.session.session_key, settings.SESSION_COOKIE_AGE)
        return response
