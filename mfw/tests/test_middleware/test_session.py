# vim: set fileencoding=utf-8 :
"""
Unittest module of ...


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
from django.http import HttpResponse
from django.test import TestCase
from django.test import RequestFactory
from mfw.tests import user_agents
from mfw.tests.override_settings import override_settings
from mfw.middleware.device import DeviceDetectionMiddleware
from mfw.middleware.session import SessionMiddleware


NOT_SUPPORT_COOKIE = {
    'HTTP_USER_AGENT': user_agents.SOFTBANK[0][5],
    'REMOTE_ADDR': user_agents.SOFTBANK[0][6],
    'HTTP_X_JPHONE_UID': 'A012345',
}
SUPPORT_COOKIE = {
    'HTTP_USER_AGENT': user_agents.SOFTBANK[1][5],
    'REMOTE_ADDR': user_agents.SOFTBANK[1][6],
    'HTTP_X_JPHONE_UID': 'A012345',
}
NOT_SUPPORT_COOKIE_NOT_RELIABLE = {
    'HTTP_USER_AGENT': user_agents.SOFTBANK[0][5],
    'REMOTE_ADDR': '127.0.0.1',
    'HTTP_X_JPHONE_UID': 'A012345',
}
NOT_SUPPORT_COOKIE_DOCOMO = {
    'HTTP_USER_AGENT': user_agents.DOCOMO[0][5],
    'REMOTE_ADDR': user_agents.DOCOMO[0][6],
    'HTTP_X_DCMGUID': 'A012345',
}


def create_session_key(meta):
    from mfw.device import detect
    from mfw.middleware.session import create_session_key as fn
    device = detect(meta)
    return fn(device.carrier, device.uid)


class MFWSessionMiddlewareTestCase(TestCase):

    urls = 'mfw.tests.urls'

    def setUp(self):
        self.factory = RequestFactory()

    def test_session_with_support_cookie(self):
        request = self.factory.get('/', **SUPPORT_COOKIE)
        response = HttpResponse('Session test')
        middleware1 = DeviceDetectionMiddleware()
        middleware2 = SessionMiddleware()
        session_key = create_session_key(SUPPORT_COOKIE)

        middleware1.process_request(request)
        middleware2.process_request(request)

        # Add new session key
        request.session['hello'] = 'world'

        response = middleware2.process_response(request, response)

        # request bundle session should not use UID for session key
        self.assertNotEqual(request.session.session_key, session_key)
        # request bundle COOKIES should not be overridden
        self.assertFalse(getattr(request.COOKIES, '_mfw_overridden', False))
        # response set_cookie method should not be overridden
        self.assertFalse(getattr(response.set_cookie, '_mfw_overridden', False))

        # start new request
        request = self.factory.get('/', **NOT_SUPPORT_COOKIE)
        response = HttpResponse('Session test')
        middleware1.process_request(request)
        middleware2.process_request(request)
        response = middleware2.process_response(request, response)

        # session should be saved correctly
        # but django's SessionMiddleware use cookies to store generated
        # session_key and RequestFactory seems to not handle cookie
        # thus actually session is not saved with in this test.
        #self.assertEqual(request.session.get('hello', None), 'world')

    def test_session_with_not_support_cookie(self):
        request = self.factory.get('/', **NOT_SUPPORT_COOKIE)
        response = HttpResponse('Session test')
        middleware1 = DeviceDetectionMiddleware()
        middleware2 = SessionMiddleware()
        session_key = create_session_key(NOT_SUPPORT_COOKIE)

        middleware1.process_request(request)
        middleware2.process_request(request)

        # Add new session key
        request.session['hello'] = 'world'

        response = middleware2.process_response(request, response)

        # request bundle session should use UID for session key
        self.assertEqual(request.session.session_key, session_key)
        # request bundle COOKIES should be overridden
        self.assertTrue(getattr(request.COOKIES, '_mfw_overridden', False))
        # response set_cookie method should be overridden
        self.assertTrue(getattr(response.set_cookie, '_mfw_overridden', False))

        # start new request
        request = self.factory.get('/', **NOT_SUPPORT_COOKIE)
        response = HttpResponse('Session test')
        middleware1.process_request(request)
        middleware2.process_request(request)
        response = middleware2.process_response(request, response)

        # session should be saved correctly
        self.assertEqual(request.session.get('hello', None), 'world')

    def test_session_with_not_support_cookie_not_reliable(self):
        with override_settings(MFW_SESSION_TRUST_NON_RELIABLE_DEVICE=False):
            request = self.factory.get('/', **NOT_SUPPORT_COOKIE_NOT_RELIABLE)
            response = HttpResponse('Session test')
            middleware1 = DeviceDetectionMiddleware()
            middleware2 = SessionMiddleware()
            session_key = create_session_key(NOT_SUPPORT_COOKIE_NOT_RELIABLE)

            middleware1.process_request(request)
            middleware2.process_request(request)

            # Add new session key
            request.session['hello'] = 'world'

            response = middleware2.process_response(request, response)

            # request bundle session should not use UID for session key
            # because the device is not reliable
            self.assertNotEqual(request.session.session_key, session_key)
            # request bundle COOKIES should not be overridden
            # because the device is not reliable
            self.assertFalse(getattr(request.COOKIES, '_mfw_overridden', False))
            # response set_cookie method should not be overridden
            # because the device is not reliable
            self.assertFalse(getattr(response.set_cookie, '_mfw_overridden', False))

        with override_settings(MFW_SESSION_TRUST_NON_RELIABLE_DEVICE=True):
            request = self.factory.get('/', **NOT_SUPPORT_COOKIE_NOT_RELIABLE)
            response = HttpResponse('Session test')
            middleware1 = DeviceDetectionMiddleware()
            middleware2 = SessionMiddleware()
            session_key = create_session_key(NOT_SUPPORT_COOKIE_NOT_RELIABLE)

            middleware1.process_request(request)
            middleware2.process_request(request)

            # Add new session key
            request.session['hello'] = 'world'

            response = middleware2.process_response(request, response)

            # request bundle session should use UID for session key
            # because the device is not reliable but
            # MFW_SESSION_TRUST_NON_RELIABLE_DEVICE set True
            self.assertEqual(request.session.session_key, session_key)
            # request bundle COOKIES should not be overridden
            # because the device is not reliable but
            # MFW_SESSION_TRUST_NON_RELIABLE_DEVICE set True
            self.assertTrue(getattr(request.COOKIES, '_mfw_overridden', False))
            # response set_cookie method should not be overridden
            # because the device is not reliable but
            # MFW_SESSION_TRUST_NON_RELIABLE_DEVICE set True
            self.assertTrue(getattr(response.set_cookie, '_mfw_overridden', False))

    def test_session_with_not_support_cookie_docomo(self):
        d = dict(NOT_SUPPORT_COOKIE_DOCOMO)
        del d['HTTP_X_DCMGUID']
        request = self.factory.get('/', **d)
        response = HttpResponse('Session test')
        middleware1 = DeviceDetectionMiddleware()
        middleware2 = SessionMiddleware()

        middleware1.process_request(request)
        response = middleware2.process_request(request)

        # without '?guid=pn', DoCoMo server does not return UID thus
        # the middleware redirect when no ?guid=on is found
        self.assertNotEqual(response, None)
        response.client = self.client   # monkey patch
        self.assertRedirects(response, '/?guid=on')

        request = self.factory.get('/?guid=on', **NOT_SUPPORT_COOKIE_DOCOMO)
        response = HttpResponse('Session test')
        middleware1 = DeviceDetectionMiddleware()
        middleware2 = SessionMiddleware()

        middleware1.process_request(request)
        response = middleware2.process_request(request)

        # with guid=on, the middleware should not redirect
        self.assertEqual(response, None)

    def test_csrf_protection_pass_with_not_support_cookie(self):
        from django.middleware.csrf import get_token
        from mfw.middleware.csrf import CsrfViewMiddleware

        # request with GET
        request = self.factory.get('/', **NOT_SUPPORT_COOKIE)
        response = HttpResponse('Session test')
        middleware1 = DeviceDetectionMiddleware()
        middleware2 = SessionMiddleware()
        middleware3 = CsrfViewMiddleware()

        middleware1.process_request(request)
        middleware2.process_request(request)
        middleware3.process_view(request, None, (), {})

        # Simulate {% csrf_token %} templatetag. It is required to
        # set request.META['CSRF_COOKIE_USED'] = True
        csrf_token = str(get_token(request))
        self.assertEqual(request.META.get('CSRF_COOKIE', None), csrf_token)
        self.assertEqual(request.META.get('CSRF_COOKIE_USED', False), True)

        # bottom up for response phase
        response = middleware3.process_response(request, response)
        response = middleware2.process_response(request, response)
        
        # new request with POST
        data = {'csrfmiddlewaretoken': csrf_token}
        request = self.factory.post('/', data, **NOT_SUPPORT_COOKIE)

        middleware1.process_request(request)
        middleware2.process_request(request)
        response = middleware3.process_view(request, None, (), {})

        # if csrf protection worked, response will be HttpResponseForbidden
        self.assertEqual(request.META.get('CSRF_COOKIE', None), csrf_token)
        self.assertEqual(request.META.get('CSRF_COOKIE_USED', False), False)
        self.assertEqual(response, None)

    def test_csrf_protection_fail_with_not_support_cookie(self):
        from django.http import HttpResponseForbidden
        from django.middleware.csrf import get_token
        from mfw.middleware.csrf import CsrfViewMiddleware

        # request with GET
        request = self.factory.get('/', **NOT_SUPPORT_COOKIE)
        response = HttpResponse('Session test')
        middleware1 = DeviceDetectionMiddleware()
        middleware2 = SessionMiddleware()
        middleware3 = CsrfViewMiddleware()

        middleware1.process_request(request)
        middleware2.process_request(request)
        middleware3.process_view(request, None, (), {})

        # Simulate {% csrf_token %} templatetag. It is required to
        # set request.META['CSRF_COOKIE_USED'] = True
        csrf_token = str(get_token(request))
        self.assertEqual(request.META.get('CSRF_COOKIE', None), csrf_token)
        self.assertEqual(request.META.get('CSRF_COOKIE_USED', False), True)

        # bottom up for response phase
        response = middleware3.process_response(request, response)
        response = middleware2.process_response(request, response)

        # new request with POST
        data = {'csrfmiddlewaretoken': 'wrong-csrf-token'}
        request = self.factory.post('/', data, **NOT_SUPPORT_COOKIE)

        middleware1.process_request(request)
        middleware2.process_request(request)
        response = middleware3.process_view(request, None, (), {})

        # if csrf protection worked, response will be HttpResponseForbidden
        self.assertEqual(request.META.get('CSRF_COOKIE', None), csrf_token)
        self.assertEqual(request.META.get('CSRF_COOKIE_USED', False), False)
        self.assertNotEqual(response, None)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(isinstance(response, HttpResponseForbidden))
