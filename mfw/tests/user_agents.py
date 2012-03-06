# vim: set fileencoding=utf-8 :
"""
Sample HTTP_USER_AGENT


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

INTERNET_EXPLORER = (
        # Kind, Name, Model, Version, USER_AGENT
        ('browser', 'Explorer', 'Windows', '4.0', 'Mozilla/4.0 (compatible; MSIE 4.01; Windows NT)'),
        ('browser', 'Explorer', 'Mac', '4.5', 'Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)'),
        ('browser', 'Explorer', 'Windows', '5.0', 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; .NET CLR 1.1.4322)'),
        ('browser', 'Explorer', 'Mac', '5.2', 'Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC)'),
        ('browser', 'Explorer', 'Windows', '5.5', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; by TSG)'),
        ('browser', 'Explorer', 'Windows', '6.0', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows XP)'),
        ('browser', 'Explorer', 'Windows', '7.0', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'),
        ('browser', 'Explorer', 'Windows', '8.0', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1;'),
        ('browser', 'Explorer', 'Windows', '9.0', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)'),
        ('browser', 'Explorer', 'Windows', '10.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'),
    )

GOOGLE_CHROME = (
        ('browser', 'Chrome', 'Windows', '1.0', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.48 Safari/525.19',),
        ('browser', 'Chrome', 'Windows', '2.0', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5',),
        ('browser', 'Chrome', 'Windows', '3.0', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.38 Safari/532.0',),
        ('browser', 'Chrome', 'Mac', '11.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.71 Safari/534.24',),
        ('browser', 'Chrome', 'Mac', '11.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.2 Chrome/11.0.700.2 Safari/534.24',),
        ('browser', 'Chrome', 'Windows', '11.0', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.65 Safari/534.24',),
        ('browser', 'Chrome', 'Mac', '12.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30',),
        ('browser', 'Chrome', 'Windows', '13.0', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1',),
        ('browser', 'Chrome', 'Mac', '13.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) RockMelt/0.9.64.361 Chrome/13.0.782.218 Safari/535.1',),
        ('browser', 'Chrome', 'Mac', '13.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1',),
        ('browser', 'Chrome', 'Mac', '13.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1',),
        ('browser', 'Chrome', 'Mac', '14.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1',),
        ('browser', 'Chrome', 'Windows', '14.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1',),
        ('browser', 'Chrome', 'Windows', '15.0', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',),
        ('browser', 'Chrome', 'Linux', '15.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/10.04 Chromium/15.0.874.106 Chrome/15.0.874.106 Safari/535.2',),
        ('browser', 'Chrome', 'Mac', '15.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.106 Safari/535.2',),
        ('browser', 'Chrome', 'Windows', '16.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7',),
        ('browser', 'Chrome', 'Mac', '16.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7',),
    )

LUNASCAPE = (
        ('browser', 'Lunascape', 'Windows', '4.7', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618; Lunascape 4.7.3)',),
        ('browser', 'Lunascape', 'Windows', '5.0', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Lunascape 5.0 alpha2)',),
        ('browser', 'Lunascape', 'Windows', '5.0', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 5.0 alpha2)',),
        ('browser', 'Lunascape', 'Windows', '5.0', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; Tablet PC 2.0; Lunascape 5.0 alpha2)',),
        ('browser', 'Lunascape', 'Windows', '6.5', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAGW; .NET4.0C; Lunascape 6.5.8.24780)',),
    )

FIREFOX = (
        ('browser', 'Firefox', 'Windows', '6.0', 'Mozilla/5.0 (Windows NT 5.1; rv:6.0) Gecko/20100101 Firefox/6.0',),
        ('browser', 'Firefox', 'Mac', '6.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:6.0.2) Gecko/20100101 Firefox/6.0.2',),
        ('browser', 'Firefox', 'Windows', '7.0', 'Mozilla/5.0 (Windows NT 6.0; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',),
        ('browser', 'Firefox', 'Mac', '7.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',),
        ('browser', 'Firefox', 'Mac', '8.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',),
        ('browser', 'Firefox', 'Windows', '9.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1',),
        ('browser', 'Firefox', 'Mac', '9.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:9.0.1) Gecko/20100101 Firefox/9.0.1',),
    )

SAFARI = (
        ('browser', 'Safari', 'Mac', '3.1', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; ja-jp) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13',),
        ('browser', 'Safari', 'Mac', '3.1', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3; ja-jp) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20',),
        ('browser', 'Safari', 'Mac', '3.1', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; ja-jp) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.22',),
        ('browser', 'Safari', 'Mac', '3.2', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; ja-jp) AppleWebKit/525.26.2 (KHTML, like Gecko) Version/3.2 Safari/525.26.12',),
        ('browser', 'Safari', 'Mac', '3.2', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; ja-jp) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1',),
        ('browser', 'Safari', 'Mac', '4.0', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; ja-jp) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16',),
        ('browser', 'Safari', 'Mac', '4.0', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; ja-jp) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',),
        ('browser', 'Safari', 'Mac', '4.0', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; ja-jp) AppleWebKit/531.21.11 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',),
        ('browser', 'Safari', 'Mac', '5.0', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16',),
        ('browser', 'Safari', 'Mac', '5.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.52.7 (KHTML, like Gecko) Version/5.1.2 Safari/534.52.7',),
    )

OPERA = (
        ('browser', 'Opera', 'Windows', '9.0', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ja) Opera 9.00',),
        ('browser', 'Opera', 'Windows', '9.0', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.00',),
        ('browser', 'Opera', 'Windows', '9.0', 'Opera/9.00 (Windows NT 5.1; U; ja)',),
        ('browser', 'Opera', 'Windows', '9.6', 'Opera/9.60 (Windows NT 5.1; U; ja) Presto/2.1.1',),
        ('browser', 'Opera', 'Windows', '9.6', 'Opera/9.61 (Windows NT 5.1; U; ja) Presto/2.1.1',),
        ('browser', 'Opera', 'Windows', '9.6', 'Opera/9.62 (Windows NT 5.1; U; ja) Presto/2.1.1',),
    )

IPHONE = (
        ('smartphone', 'iOS', 'iPhone', '', 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1C28 Safari/419.3',),
        ('smartphone', 'iOS', 'iPhone', '2.1', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F136 Safari/525.20',),
        ('smartphone', 'iOS', 'iPhone', '3.1', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; ja-jp) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16',),
        ('smartphone', 'iOS', 'iPhone', '4.3', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',),
        ('smartphone', 'iOS', 'iPhone', '5.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405 Safari/7534.48.3',),
    )

IPOD = (
        ('smartphone', 'iOS', 'iPod', '', 'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A100a Safari/419.3',),
        ('smartphone', 'iOS', 'iPod', '2.1', 'Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20',),
        ('smartphone', 'iOS', 'iPod', '4.1', 'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B118 Safari/6531.22.7',),
        ('smartphone', 'iOS', 'iPod', '4.2', 'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_2_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',),
        ('smartphone', 'iOS', 'iPod', '4.3', 'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_5 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',),
        ('smartphone', 'iOS', 'iPod', '5.0', 'Mozilla/5.0 (iPod; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3',),
    )

IPAD = (
        ('smartphone', 'iOS', 'iPad', '3.2', 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10',),
        ('smartphone', 'iOS', 'iPad', '3.2', 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405',),
        ('smartphone', 'iOS', 'iPad', '4.2', 'Mozilla/5.0 (iPad; U; CPU OS 4_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C134',),
        ('smartphone', 'iOS', 'iPad', '4.3', 'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5',),
        ('smartphone', 'iOS', 'iPad', '4.3', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',),
        ('smartphone', 'iOS', 'iPad', '4.3', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_2 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5',),
        ('smartphone', 'iOS', 'iPad', '4.3', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',),
        ('smartphone', 'iOS', 'iPad', '4.3', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_4 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5',),
        ('smartphone', 'iOS', 'iPad', '4.3', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',),
        ('smartphone', 'iOS', 'iPad', '5.0', 'Mozilla/5.0 (iPad; CPU OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3',),
    )

ANDROID = (
        ('smartphone', 'Android', 'GDDJ-09', '1.5', 'Mozilla/5.0 (Linux; U; Android 1.5; ja-jp; GDDJ-09 Build/CDB56) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1',),
        ('smartphone', 'Android', 'IS01', '1.6', 'Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; IS01 Build/S3082) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1',),
        ('smartphone', 'Android', 'IS01', '1.6', 'Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; IS01 Build/SA180) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1',),
        ('smartphone', 'Android', 'Docomo HT-03A', '1.6', 'Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; Docomo HT-03A Build/DRD08) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1',),
        ('smartphone', 'Android', 'SonyEricssonSO-01B', '1.6', 'Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; SonyEricssonSO-01B Build/R1EA029) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1',),
        ('smartphone', 'Android', 'generic', '1.6', 'Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; generic Build/Donut) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1',),
        ('smartphone', 'Android', 'SonyEricssonSO-01B', '2.1', 'Mozilla/5.0 (Linux; U; Android 2.1-update1; ja-jp; SonyEricssonSO-01B Build/2.0.2.B.0.29) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',),
        ('smartphone', 'Android', 'Full Android', '2.2', 'Mozilla/5.0 (Linux; U; Android 2.2.1; ja-jp; Full Android Build/MASTER) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',),
        ('smartphone', 'Android', 'IS03', '2.2', 'Mozilla/5.0 (Linux; U; Android 2.2.1; ja-jp; IS03 Build/S9090) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',),
        ('smartphone', 'Android', 'SC-02C', '2.3', 'Mozilla/5.0 (Linux; U; Android 2.3.3; ja-jp; SC-02C Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',),
        ('smartphone', 'Android', 'INFOBAR A01', '2.3', 'Mozilla/5.0 (Linux; U; Android 2.3.3; ja-jp; INFOBAR A01 Build/S9081) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',),
        ('smartphone', 'Android', '001HT', '2.3', 'Mozilla/5.0 (Linux; U; Android 2.3.3; ja-jp; 001HT Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',),
        ('smartphone', 'Android', 'SonyEricssonX10i', '2.3', 'Mozilla/5.0 (Linux; U; Android 2.3.3; ja-jp; SonyEricssonX10i Build/3.0.1.G.0.75) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',),
        ('smartphone', 'Android', 'SonyEricssonIS11S', '2.3', 'Mozilla/5.0 (Linux; U; Android 2.3.4; ja-jp; SonyEricssonIS11S Build/4.0.1.B.0.112) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',),
        ('smartphone', 'Android', 'IS05', '2.3', 'Mozilla/5.0 (Linux; U; Android 2.3.4; ja-jp; IS05 Build/S9290) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',),
        ('smartphone', 'Android', 'F-05D', '2.3', 'Mozilla/5.0 (Linux; U; Android 2.3.5; ja-jp; F-05D Build/F0001) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',),
        ('smartphone', 'Android', 'T-01D', '2.3', 'Mozilla/5.0 (Linux; U; Android 2.3.5; ja-jp; T-01D Build/F0001) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',),
        ('smartphone', 'Android', 'MZ604', '3.0', 'Mozilla/5.0 (Linux; U; Android 3.0.1; ja-jp; MZ604 Build/H.6.2-20) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',),
        ('smartphone', 'Android', 'K1', '3.1', 'Mozilla/5.0 (Linux; U; Android 3.1; en-us; K1 Build/HMJ37) AppleWebKit/534.13(KHTML, like Gecko) Version/4.0 Safari/534.13',),
        ('smartphone', 'Android', 'AT100', '3.1', 'Mozilla/5.0 (Linux; U; Android 3.1; ja-jp; AT100 Build/HMJ37) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',),
        ('smartphone', 'Android', 'Sony Tablet S', '3.1', 'Mozilla/5.0 (Linux; U; Android 3.1; ja-jp; Sony Tablet S Build/THMAS10000) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',),
        ('smartphone', 'Android', 'SC-01D', '3.2', 'Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; SC-01D Build/MASTER) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',),
        ('smartphone', 'Android', 'AT1S0', '3.2', 'Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; AT1S0 Build/HTJ85B) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',),
        ('smartphone', 'Android', 'F-01D', '3.2', 'Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; F-01D Build/F0001) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',),
        ('smartphone', 'Android', 'Sony Tablet S', '3.2', 'Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; Sony Tablet S Build/THMAS11000) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',),
        ('smartphone', 'Android', 'A01SH', '3.2', 'Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; A01SH Build/HTJ85B) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1',),
        ('smartphone', 'Android', 'Transformer TF101', '3.2', 'Mozilla/5.0 (Linux; U; Android 3.2.1; ja-jp; Transformer TF101 Build/HTK75) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',),
        ('smartphone', 'Android', 'Galaxy Nexus', '4.0', 'Mozilla/5.0 (Linux; U; Android 4.0.1; ja-jp; Galaxy Nexus Build/ITL41D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',),
        ('smartphone', 'Android', 'Opera Mobi', '2.3', 'Opera/9.80 (Android 2.3.3; Linux; Opera Mobi/ADR-1111101157; U; ja) Presto/2.9.201 Version/11.50',),
        ('smartphone', 'Android', 'Opera Tablet', '3.2', 'Opera/9.80 (Android 3.2.1; Linux; Opera Tablet/ADR-1109081720; U; ja) Presto/2.8.149 Version/11.10',),
        ('smartphone', 'Android', 'Firefox', '9.0', 'Mozilla/5.0 (Android; Linux armv7l; rv:9.0) Gecko/20111216 Firefox/9.0 Fennec/9.0',),
    )

WINDOWS_PHONE = (
        ('smartphone', 'WindowsPhone', '', '6.5', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; KDDI-TS01; Windows Phone 6.5.3.5)',),
        ('smartphone', 'WindowsPhone', '', '7.5', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; FujitsuToshibaMobileCommun; IS12T; KDDI)',),
    )

BLACK_BERRY = (
        ('smartphone', 'BlackBerry', '', '4.6', 'BlackBerry9000/4.6.0.294 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/220',),
        ('smartphone', 'BlackBerry', '', '5.0', 'BlackBerry9300/5.0.0.1007 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/220',),
        ('smartphone', 'BlackBerry', '', '5.0', 'BlackBerry9700/5.0.0.1014 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/220',),
        ('smartphone', 'BlackBerry', '', '6.0', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; ja) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.570 Mobile Safari/534.8+',),
        ('smartphone', 'BlackBerry', '', '6.0', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9780; ja) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.587 Mobile Safari/534.8+',),
        ('smartphone', 'BlackBerry', '', '7.1', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; ja) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.74 Mobile Safari/534.11+',),
        ('smartphone', 'BlackBerry', 'Opera Mini', '9.8', 'Opera/9.80 (BlackBerry; Opera Mini/6.1.25376/26.958; U; en) Presto/2.8.119 Version/10.54',),
    )

DOCOMO_IP = '210.153.84.0'
DOCOMO = (
        # Kind, Name, Model, Version, Cookie, HTTP_USER_AGENT, REMOTE_ADDR, Additional
        ('mobilephone', 'DoCoMo', 'D502i', '', False, 'DoCoMo/1.0/D502i', DOCOMO_IP, {'HTTP_X_DCMGUID': 'A12345'}),
        ('mobilephone', 'DoCoMo', 'F06B', '', True, 'DoCoMo/2.0 F06B(c500;TB;W24H16)', DOCOMO_IP, {'HTTP_X_DCMGUID': 'A12345'}),
        ('mobilephone', 'DoCoMo', 'F06B', '', True, 'DoCoMo/2.0 F06B(c500;TB;W24H16)', '127.0.0.1', {'HTTP_X_DCMGUID': 'A12345'}),
    )

KDDI_IP = '210.230.128.224'
KDDI = (
        ('mobilephone', 'KDDI', 'SA31', '', True, 'KDDI-SA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0', KDDI_IP, {'HTTP_X_UP_SUBNO': 'A12345'}),
        ('mobilephone', 'KDDI', 'SA31', '', True, 'SIE-SA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0', KDDI_IP, {'HTTP_X_UP_SUBNO': 'A12345'}),
        ('mobilephone', 'KDDI', 'SA31', '', True, 'KDDI-SA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0', '127.0.0.1', {'HTTP_X_UP_SUBNO': 'A12345'}),
    )

SOFTBANK_IP = '123.108.237.0'
SOFTBANK = (
        ('mobilephone', 'Softbank', 'J-SH02', '', False, 'J-PHONE/2.0/J-SH02', SOFTBANK_IP, {'HTTP_X_JPHONE_UID': 'A12345'}),
        ('mobilephone', 'Softbank', 'V803T', '', True, 'Vodafone/1.0/V803T/TJ001[/Serial] Browser/VF-Browser/1.0', SOFTBANK_IP, {'HTTP_X_JPHONE_UID': 'A12345'}),
        ('mobilephone', 'Softbank', '002Pe', '', True, 'SoftBank/1.0/002Pe/PJP10[/Serial] Browser/NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1', SOFTBANK_IP, {'HTTP_X_JPHONE_UID': 'A12345'}),
        ('mobilephone', 'Softbank', '002Pe', '', True, 'SoftBank/1.0/002Pe/PJP10[/Serial] Browser/NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1', '127.0.0.1', {'HTTP_X_JPHONE_UID': 'A12345'}),
    )
