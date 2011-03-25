#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
from django.middleware.csrf import CsrfViewMiddleware as _CsrfViewMiddleware, \
                                   CsrfResponseMiddleware, \
                                   CsrfMiddleware as _CsrfMiddleware, \
                                   _get_failure_view, _sanitize_token, \
                                   _get_new_csrf_key, _make_legacy_session_token, \
                                   REASON_NO_REFERER, REASON_BAD_REFERER, \
                                   REASON_NO_COOKIE, REASON_NO_CSRF_COOKIE, REASON_BAD_TOKEN

from ..conf import settings
from ..core import detect

def _get_device(request):
    device = getattr(request, 'device', detect(request.META))
    return device

class CsrfViewMiddleware(_CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        device = _get_device(request)
        
        if device.support_cookie:
            # Use django's default CsrfViewMiddleware for device support cookie
            return super(CsrfViewMiddleware, self).process_view(request, callback, callback_args, callback_kwargs)
        
        if getattr(request, 'csrf_processing_done', False):
            return None
        
        reject = lambda s: _get_failure_view()(request, reason=s)
        def accept():
            # Avoid checking the request twice by adding a custom attribute to
            # request.  This will be relevant when both decorator and middleware
            # are used.
            request.csrf_processing_done = True
            return None

        # If the user doesn't have a CSRF cookie, generate one and store it in the
        # request, so it's available to the view.  We'll store it in a cookie when
        # we reach the response.
        try:
            # In case of cookies from untrusted sources, we strip anything
            # dangerous at this point, so that the cookie + token will have the
            # same, sanitized value.
            request.META["CSRF_COOKIE"] = _sanitize_token(request.session.get(settings.CSRF_COOKIE_NAME, u""))
            session_is_new = False
        except KeyError:
            # No cookie, so create one.  This will be sent with the next
            # response.
            request.META["CSRF_COOKIE"] = _get_new_csrf_key()
            # Set a flag to allow us to fall back and allow the session id in
            # place of a CSRF cookie for this request only.
            session_is_new = True

        # Wait until request.META["CSRF_COOKIE"] has been manipulated before
        # bailing out, so that get_token still works
        if getattr(callback, 'csrf_exempt', False):
            return None

        if request.method == 'POST':
            if getattr(request, '_dont_enforce_csrf_checks', False):
                # Mechanism to turn off CSRF checks for test suite.  It comes after
                # the creation of CSRF cookies, so that everything else continues to
                # work exactly the same (e.g. cookies are sent etc), but before the
                # any branches that call reject()
                return accept()

            if request.is_ajax():
                # .is_ajax() is based on the presence of X-Requested-With.  In
                # the context of a browser, this can only be sent if using
                # XmlHttpRequest.  Browsers implement careful policies for
                # XmlHttpRequest:
                #
                #  * Normally, only same-domain requests are allowed.
                #
                #  * Some browsers (e.g. Firefox 3.5 and later) relax this
                #    carefully:
                #
                #    * if it is a 'simple' GET or POST request (which can
                #      include no custom headers), it is allowed to be cross
                #      domain.  These requests will not be recognized as AJAX.
                #
                #    * if a 'preflight' check with the server confirms that the
                #      server is expecting and allows the request, cross domain
                #      requests even with custom headers are allowed. These
                #      requests will be recognized as AJAX, but can only get
                #      through when the developer has specifically opted in to
                #      allowing the cross-domain POST request.
                #
                # So in all cases, it is safe to allow these requests through.
                return accept()

            if request.is_secure():
                # Strict referer checking for HTTPS
                referer = request.META.get('HTTP_REFERER')
                if referer is None:
                    return reject(REASON_NO_REFERER)

                # The following check ensures that the referer is HTTPS,
                # the domains match and the ports match.  This might be too strict.
                good_referer = 'https://%s/' % request.get_host()
                if not referer.startswith(good_referer):
                    return reject(REASON_BAD_REFERER %
                                  (referer, good_referer))

            # If the user didn't already have a CSRF session, then fall back to
            # the Django 1.1 method (hash of session ID), so a request is not
            # rejected if the form was sent to the user before upgrading to the
            # Django 1.2 method (session independent nonce)
            if session_is_new:
                try:
                    session_id = request.session.get(settings.SESSION_COOKIE_NAME)
                    csrf_token = _make_legacy_session_token(session_id)
                except KeyError:
                    # No CSRF cookie and no session cookie. For POST requests,
                    # we insist on a CSRF cookie, and in this way we can avoid
                    # all CSRF attacks, including login CSRF.
                    return reject(REASON_NO_COOKIE)
            else:
                csrf_token = request.META["CSRF_COOKIE"]

            # check incoming token
            request_csrf_token = request.POST.get('csrfmiddlewaretoken', None)
            if request_csrf_token != csrf_token:
                if session_is_new:
                    # probably a problem setting the CSRF cookie
                    return reject(REASON_NO_CSRF_COOKIE)
                else:
                    return reject(REASON_BAD_TOKEN)
        return accept()
    
    def process_response(self, request, response):
        device = _get_device(request)
        
        if device.support_cookie:
            # Use django's default CsrfViewMiddleware for device support cookie
            return super(CsrfViewMiddleware, self).process_response(request, response)
        
        if getattr(response, 'csrf_processing_done', False):
            return response

        # If CSRF_SESSION is unset, then CsrfViewMiddleware.process_view was
        # never called, probaby because a request middleware returned a response
        # (for example, contrib.auth redirecting to a login page).
        if request.META.get("CSRF_COOKIE") is None:
            return response

        if not request.META.get("CSRF_COOKIE_USED", False):
            return response

        # Set the CSRF cookie even if it's already set, so we renew the expiry timer.
        request.session[settings.CSRF_COOKIE_NAME] = request.META['CSRF_COOKIE']
        response.csrf_processing_done = True
        return response

class CsrfMiddleware(_CsrfMiddleware):
    def __init__(self):
        self.response_middleware = CsrfResponseMiddleware()
        self.view_middleware = CsrfViewMiddleware()
