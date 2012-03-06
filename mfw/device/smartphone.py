# vim: set fileencoding=utf-8 :
"""
Smartphone


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
from mfw.device.base import UserAgentRegexPatternDevice

class Smartphone(UserAgentRegexPatternDevice):
    _support_cookie = True
    _kind = 'smartphone'
    _patterns = (
        ('iOS', re.compile(r"Mozilla/[\d\.]* \((?P<model>[^;]*); .*CPU like Mac OS X")),
        ('iOS', re.compile(r"Mozilla/[\d\.]* \((?P<model>[^;]*); .*CPU iPhone OS (?P<version>[\w_]*) like Mac OS X")),
        ('iOS', re.compile(r"Mozilla/[\d\.]* \((?P<model>[^;]*); .*CPU OS (?P<version>[\w_]*) like Mac OS X")),
        ('Android', re.compile(r"Mozilla/[\d\.]* \(Linux; U; Android (?P<version>[^;]*); [^;]*; (?P<model>[^;\)]*) Build/.*\)")),
        ('Android', re.compile(r"Opera/[\d\.]* \(Android (?P<version>[^;]*); Linux; (?P<model>[^;\)\/]*)")),
        ('Android', re.compile(r"Mozilla/[\d\.]* \(Android; Linux .*\) Gecko/\d* (?P<model>[^/]*)/(?P<version>[\d\.]*)")),
        ('WindowsPhone', re.compile(r"Mozilla/[\d\.]* \(compatible; MSIE [\d\.]*; Windows Phone OS (?P<version>[\d\.]*);")),
        ('WindowsPhone', re.compile(r"Mozilla/[\d\.]* \(compatible; MSIE [\d\.]*; .* Windows Phone (?P<version>[\d\.]*)\)")),
        ('BlackBerry', re.compile(r"BlackBerry\d*/(?P<version>[\d\.]*)")),
        ('BlackBerry', re.compile(r"Mozilla/[\d\.]* \(BlackBerry; .*\) .* Version/(?P<version>[\d\.]*)")),
        ('BlackBerry', re.compile(r"Opera/(?P<version>[\d\.]*) \(BlackBerry; (?P<model>[^/]*)")),
    )

    def __init__(self, **kwargs):
        super(Smartphone, self).__init__(**kwargs)
        if self.version and '_' in self.version:
            self._version = self._version.replace('_', '.')
