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
from django.test import TestCase
from mfw.tests.mock import Mock
from mfw.tests.override_settings import override_settings
from mfw.tests import user_agents
from mfw.middleware.device import DeviceDetectionMiddleware
from mfw.device.base import Device

@override_settings(MIDDLEWARE_CLASSES=(
    'mfw.middleware.device.DeviceDetectionMiddleware',
    'django.middleware.common.CommonMiddleware',
), TEMPLATE_CONTEXT_PROCESSORS=())
class MFWDeviceDetectionMiddlewareTestCase(TestCase):

    def test_standalone(self):
        request_class = Mock('django.http.HttpRequest')
        request = request_class()

        for user_agent in user_agents.INTERNET_EXPLORER:
            kind, name, model, version, user_agent = user_agent

            request.META = {
                    'HTTP_USER_AGENT': user_agent
                }

            middleware = DeviceDetectionMiddleware()
            middleware.process_request(request)

            self.assertTrue(isinstance(request.device, Device))
            self.assertEqual(request.device.kind, kind)
            self.assertEqual(request.device.name, name)
            self.assertEqual(request.device.model, model)
            self.assertTrue(request.device.version.startswith(version))

