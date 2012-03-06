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
from mfw.tests.mock import Mock
from mfw.middleware.encoding import DeviceEncodingMiddleware


Device = Mock('mfw.device.base.Device')

class MFWDeviceEncodingMiddlewareTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_standalone(self):
        request = self.factory.get('/')
        request.device = Device()
        request.device.encoding = 'cp932'
        response = HttpResponse(u'\u3042')
        middleware = DeviceEncodingMiddleware()

        middleware.process_request(request)
        response = middleware.process_response(request, response)

        self.assertTrue(getattr(response, '_mfw_encoded', False))
        self.assertEqual(response.content, "\x82\xa0")
        self.assertEqual(response['content-type'], 'application/xhtml+xml; charset=cp932')

    def test_standalone_get(self):
        dict_info = {
                'a': '\x82\xa0',
                'b': '\x82\xa0',
            }
        request = self.factory.get('/', dict_info)
        request.device = Device()
        request.device.encoding = 'cp932'
        response = HttpResponse('Encoding test')
        middleware = DeviceEncodingMiddleware()

        middleware.process_request(request)
        response = middleware.process_response(request, response)

        self.assertTrue(getattr(response, '_mfw_encoded', False))
        self.assertEqual(request.GET['a'], u"\u3042")
        self.assertEqual(request.GET['b'], u"\u3042")
