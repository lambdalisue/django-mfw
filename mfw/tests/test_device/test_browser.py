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

class MFWDeviceBrowserTestCase(TestCase):
    def test_internet_explorer(self):
        USER_AGENTS = (
                'Mozilla/4.0 (compatible; MSIE 4.01; Windows NT)',                          # Ver 4.x (Win)
                'Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)',                          # Ver 4.x (Mac)
                'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; .NET CLR 1.1.4322)',   # Ver 5.x (Win)
                'Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC)',                         # Ver 5.x (Mac)
                'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; by TSG)',               # Ver 5.5
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows XP)',                           # Ver 6.x
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',                       # Ver 7.x
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1;',                       # Ver 8.x
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',          # Ver 9.x
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',         # Ver 10.x
            )
        VERSIONS = (
                '4.01', '4.5', '5.01', '5.23',
                '5.5', '6.0', '7.0', '8.0', '9.0',
                '10.0'
            )
        for i, user_agent in enumerate(USER_AGENTS):
            meta = {'HTTP_USER_AGENT': user_agent}
            device = detect(meta)

            self.assertEqual(device.kind, 'browser')
            self.assertEqual(device.name, 'Explorer')
            self.assertEqual(device.model, None)
            self.assertEqual(device.version, VERSIONS[i])

    def test_google_chrome(self):
        USER_AGENTS = (
                # Beta 1
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.48 Safari/525.19',
                # Ver 2
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5',
                # Ver 3
                'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.38 Safari/532.0',
                # Ver 11
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.71 Safari/534.24',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.2 Chrome/11.0.700.2 Safari/534.24',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.65 Safari/534.24',
                # Ver 12
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30 ChromePlus/1.6.3.1',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30',
                # Ver 13
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) RockMelt/0.9.64.361 Chrome/13.0.782.218 Safari/535.1',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1',
                # Ver 14
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1',
                # Ver 15
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
                'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/10.04 Chromium/15.0.874.106 Chrome/15.0.874.106 Safari/535.2',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.106 Safari/535.2',
                # Ver 16
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7',
            )
        VERSIONS = (
                '1.0', '2.0', '3.0', '11.0', '11.0', '11.0',
                '12.0', '12.0', '13.0', '13.0', '13.0', '13.0',
                '14.0', '14.0', '15.0', '15.0', '15.0', '16.0',
                '16.0',
            )
        for i, user_agent in enumerate(USER_AGENTS):
            meta = {'HTTP_USER_AGENT': user_agent}
            device = detect(meta)
            self.assertEqual(device.kind, 'browser')
            self.assertEqual(device.name, 'Chrome')
            self.assertEqual(device.model, None)
            self.assertTrue(device.version.startswith(VERSIONS[i]))

    def test_lunascape(self):
        USER_AGENTS = (
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618; Lunascape 4.7.3)',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Lunascape 5.0 alpha2)',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 5.0 alpha2)',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; Tablet PC 2.0; Lunascape 5.0 alpha2)',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAGW; .NET4.0C; Lunascape 6.5.8.24780)',
            )
        VERSIONS = (
                '4.7.3', '5.0', '5.0', '5.0', '6.5.8',
            )
        for i, user_agent in enumerate(USER_AGENTS):
            meta = {'HTTP_USER_AGENT': user_agent}
            device = detect(meta)
            self.assertEqual(device.kind, 'browser')
            self.assertEqual(device.name, 'Lunascape')
            self.assertEqual(device.model, None)
            self.assertTrue(device.version.startswith(VERSIONS[i]))

    def test_firefox(self):
        USER_AGENTS = (
                'Mozilla/5.0 (Windows NT 5.1; rv:6.0) Gecko/20100101 Firefox/6.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:6.0.2) Gecko/20100101 Firefox/6.0.2',
                'Mozilla/5.0 (Windows NT 6.0; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:9.0.1) Gecko/20100101 Firefox/9.0.1',
            )
        VERSIONS = (
                '6.0', '6.0', '7.0', '7.0', '8.0', '9.0', '9.0',
            )
        for i, user_agent in enumerate(USER_AGENTS):
            meta = {'HTTP_USER_AGENT': user_agent}
            device = detect(meta)
            self.assertEqual(device.kind, 'browser')
            self.assertEqual(device.name, 'Firefox')
            self.assertEqual(device.model, None)
            self.assertTrue(device.version.startswith(VERSIONS[i]))

    def test_safari(self):
        USER_AGENTS = (
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; ja-jp) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13',
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3; ja-jp) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20',
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; ja-jp) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.22',
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; ja-jp) AppleWebKit/525.26.2 (KHTML, like Gecko) Version/3.2 Safari/525.26.12',
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; ja-jp) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1',
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; ja-jp) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16',
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; ja-jp) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; ja-jp) AppleWebKit/531.21.11 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.52.7 (KHTML, like Gecko) Version/5.1.2 Safari/534.52.7',
            )
        VERSIONS = (
                '3.1', '3.1', '3.1', '3.2', '3.2',
                '4.0', '4.0', '4.0', '5.0', '5.1',
            )
        for i, user_agent in enumerate(USER_AGENTS):
            meta = {'HTTP_USER_AGENT': user_agent}
            device = detect(meta)
            self.assertEqual(device.kind, 'browser')
            self.assertEqual(device.name, 'Safari')
            self.assertEqual(device.model, None)
            self.assertTrue(device.version.startswith(VERSIONS[i]))

    def test_opera(self):
        USER_AGENTS = (
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ja) Opera 9.00',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.00',
                'Opera/9.00 (Windows NT 5.1; U; ja)',
                'Opera/9.60 (Windows NT 5.1; U; ja) Presto/2.1.1',
                'Opera/9.61 (Windows NT 5.1; U; ja) Presto/2.1.1',
                'Opera/9.62 (Windows NT 5.1; U; ja) Presto/2.1.1',
            )
        VERSIONS = (
                '9.0', '9.0', '9.0', '9.6', '9.61', '9.62',
            )
        for i, user_agent in enumerate(USER_AGENTS):
            meta = {'HTTP_USER_AGENT': user_agent}
            device = detect(meta)
            self.assertEqual(device.kind, 'browser')
            self.assertEqual(device.name, 'Opera')
            self.assertEqual(device.model, None)
            self.assertTrue(device.version.startswith(VERSIONS[i]))

