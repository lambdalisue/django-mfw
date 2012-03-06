# vim: set fileencoding=utf-8 :
"""
Browser


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

class Browser(UserAgentRegexPatternDevice):
    _support_cookie = True
    _kind = 'browser'
    _patterns = (
        ('Lunascape', re.compile(r"Mozilla/[\d\.]* \(compatible; MSIE [\d\.]*; (?P<model>Windows|Mac|Linux) .*Lunascape (?P<version>[^\)]*)\)")),
        ('Chrome', re.compile(r"Mozilla/[\d\.]* \(.*(?P<model>Windows|Mac|Linux).*\) .* Chrome/(?P<version>[\d\.]*)")),
        ('Firefox', re.compile(r"Mozilla/[\d\.]* \(.*(?P<model>Windows|Mac|Linux).*\) .* Firefox/(?P<version>[\d\.]*)")),
        ('Safari', re.compile(r"Mozilla/[\d\.]* \(.*(?P<model>Windows|Mac|Linux).*\) .* Version/(?P<version>[\d\.]*) Safari")),
        ('Opera', re.compile(r"Mozilla/[\d\.]* \(compatible; MSIE [\d\.]*;.*(?P<model>Windows|Mac|Linux).*\) Opera (?P<version>[\d\.]*)")),
        ('Opera', re.compile(r"Opera/(?P<version>[\d\.]*) \(.*(?P<model>Windows|Macintosh|Linux).*\)")),
        ('Explorer', re.compile(r"Mozilla/[\d\.]* \(compatible; MSIE (?P<version>[\d\.]*); (?P<model>Windows|Mac|Linux*)")),
    )
