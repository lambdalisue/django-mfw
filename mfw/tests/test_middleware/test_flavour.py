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
from django.test import RequestFactory
from mfw.tests.override_settings import override_settings
from mfw.device.base import Device
from mfw.middleware.flavour import DeviceFlavourDetectionMiddleware
from mfw.middleware.flavour import parse_device
from mfw.middleware.flavour import get_flavour


class MFWDeviceFlavourDetectionMiddlewareTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_standalone(self):
        request = self.factory.get('/')
        request.device = Device(True, 'smartphone', 'iOS', 'iPhone', '5.0')
        middleware = DeviceFlavourDetectionMiddleware()

        middleware.process_request(request)

        self.assertTrue(hasattr(request, 'flavour'))
        self.assertTrue(isinstance(request.flavour, basestring))

        flavour = get_flavour()
        self.assertEqual(request.flavour, flavour)

    @override_settings(
            MFW_DEVICE_FLAVOUR_COLUMNS=lambda device: (device.kind, device.name, device.model, device.version),
            MFW_DEVICE_FLAVOUR_OVERLAP_RULES=(),
        )
    def test_parse_device(self):
        device = Device(
                support_cookie=True,
                kind='smartphone',
                name='iOS',
                model='iPhone',
                version='5.0'
            )
        self.assertEqual(parse_device(device), 'smartphone/iOS/iPhone/5.0')

        device = Device(
                support_cookie=True,
                kind='smartphone',
                name='iOS',
                model='iPhone',
                version=None
            )
        self.assertEqual(parse_device(device), 'smartphone/iOS/iPhone')

        device = Device(
                support_cookie=True,
                kind='smartphone',
                name=None,
                model='iPhone',
                version=None
            )
        self.assertEqual(parse_device(device), 'smartphone/iPhone')

    @override_settings(
            MFW_DEVICE_FLAVOUR_COLUMNS=lambda device: (device.kind, device.name, device.model, device.version),
            MFW_DEVICE_FLAVOUR_OVERLAP_RULES=(
                # Add 'fossil' to pattern name if no cookie is supported by the device
                (lambda device, previous: not device.support_cookie, lambda device, previous: ['fossil']+previous),
                # Use 'webkit' for Safari and Chrome and do not use `model` even model
                # is not None
                (lambda device, previous: device.name in ('Chrome', 'Safari'), lambda device, previous: (device.kind, 'webkit', device.version)),
            ))
    def test_parse_device_with_overlap_rules(self):
        device = Device(
                support_cookie=False,
                kind='mobilephone',
                name='DoCoMo',
                model='D502i',
                version=None,
            )
        self.assertEqual(parse_device(device), 'fossil/mobilephone/DoCoMo/D502i')

        device = Device(
                support_cookie=True,
                kind='browser',
                name='Safari',
                model='Windows',
                version='5.0',
            )
        self.assertEqual(parse_device(device), 'browser/webkit/5.0')

        device = Device(
                support_cookie=True,
                kind='browser',
                name='Chrome',
                model='Windows',
                version='5.0',
            )
        self.assertEqual(parse_device(device), 'browser/webkit/5.0')

        device = Device(
                support_cookie=True,
                kind='browser',
                name='Firefox',
                model='Windows',
                version='5.0',
            )
        self.assertEqual(parse_device(device), 'browser/Firefox/Windows/5.0')

