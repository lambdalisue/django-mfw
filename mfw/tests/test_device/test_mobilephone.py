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
from mfw.device import detect

class MFWDeviceMobilephoneTestCase(TestCase):

    def test_docomo_mova(self):
        meta = {
            'HTTP_USER_AGENT': "DoCoMo/1.0/D502i",
            'HTTP_X_DCMGUID': "XXXXXXX",
            'REMOTE_ADDR': "210.153.84.0",
        }
        device = detect(meta)
        self.assertEqual(device.name, 'docomo')
        self.assertEqual(device.model, "D502i")
        self.assertFalse(device.support_cookie)
        self.assertEqual(device.uid, "XXXXXXX")
        self.assertTrue(device.reliable)

    def test_docomo_foma(self):
        meta = {
            'HTTP_USER_AGENT': "DoCoMo/2.0 F06B(c500;TB;W24H16)",
            'HTTP_X_DCMGUID': "XXXXXXX",
            'REMOTE_ADDR': "210.153.84.0",
        }
        device = detect(meta)
        self.assertEqual(device.name, 'docomo')
        self.assertEqual(device.model, "F06B")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, "XXXXXXX")
        self.assertTrue(device.reliable)

    def test_docomo_not_reliable(self):
        meta = {
            'HTTP_USER_AGENT': "DoCoMo/2.0 F06B(c500;TB;W24H16)",
            'HTTP_X_DCMGUID': "XXXXXXX",
            'REMOTE_ADDR': "127.0.0.1",
        }
        device = detect(meta)
        self.assertEqual(device.name, 'docomo')
        self.assertEqual(device.model, "F06B")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, "XXXXXXX")
        self.assertFalse(device.reliable)

    def test_kddi(self):
        meta = {
            'HTTP_USER_AGENT': "KDDI-SA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0",
            'HTTP_X_UP_SUBNO': "XXXXXXX",
            'REMOTE_ADDR': "210.230.128.224",
        }
        device = detect(meta)
        self.assertEqual(device.name, 'kddi')
        self.assertEqual(device.model, "SA31")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, "XXXXXXX")
        self.assertTrue(device.reliable)

    def test_kddi_hdml(self):
        meta = {
            'HTTP_USER_AGENT': "SIE-SA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0",
            'HTTP_X_UP_SUBNO': "XXXXXXX",
            'REMOTE_ADDR': "210.230.128.224",
        }
        device = detect(meta)
        self.assertEqual(device.name, 'kddi')
        self.assertEqual(device.model, "SA31")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, "XXXXXXX")
        self.assertTrue(device.reliable)

    def test_kddi_not_reliable(self):
        meta = {
            'HTTP_USER_AGENT': "KDDI-SA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0",
            'HTTP_X_UP_SUBNO': "XXXXXXX",
            'REMOTE_ADDR': "127.0.0.1",
        }
        device = detect(meta)
        self.assertEqual(device.name, 'kddi')
        self.assertEqual(device.model, "SA31")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, "XXXXXXX")
        self.assertFalse(device.reliable)
    
    def test_softbank_jphone(self):
        meta = {
            'HTTP_USER_AGENT': "J-PHONE/2.0/J-SH02",
            'HTTP_X_JPHONE_UID': "XXXXXXX",
            'REMOTE_ADDR': "123.108.237.0",
        }
        device = detect(meta)
        self.assertEqual(device.name, 'softbank')
        self.assertEqual(device.model, "J-SH02")
        self.assertFalse(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertTrue(device.reliable)

    def test_softbank_vodafone(self):
        meta = {
            'HTTP_USER_AGENT': "Vodafone/1.0/V803T/TJ001[/Serial] Browser/VF-Browser/1.0",
            'HTTP_X_JPHONE_UID': "XXXXXXX",
            'REMOTE_ADDR': "123.108.237.0",
        }
        device = detect(meta)
        self.assertEqual(device.name, 'softbank')
        self.assertEqual(device.model, "V803T")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertTrue(device.reliable)

    def test_softbank_softbank(self):
        meta = {
            'HTTP_USER_AGENT': "SoftBank/1.0/002Pe/PJP10[/Serial] Browser/NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1",
            'HTTP_X_JPHONE_UID': "XXXXXXX",
            'REMOTE_ADDR': "123.108.237.0",
        }
        device = detect(meta)
        self.assertEqual(device.name, 'softbank')
        self.assertEqual(device.model, "002Pe")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, "XXXXXXX")
        self.assertTrue(device.reliable)

    def test_softbank_softbank_fake(self):
        meta = {
            'HTTP_USER_AGENT': u"SoftBank/1.0/002Pe/PJP10[/Serial] Browser/NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1",
            'HTTP_X_JPHONE_UID': u"XXXXXXX",
            'REMOTE_ADDR': u"127.0.0.1",
        }
        device = detect(meta)
        self.assertEqual(device.name, 'softbank')
        self.assertEqual(device.model, "002Pe")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, "XXXXXXX")
        self.assertFalse(device.reliable)
