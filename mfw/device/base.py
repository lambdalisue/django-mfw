# vim: set fileencoding=utf-8 :
"""
Device base


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
import uuid
from django.conf import settings

class Device(object):
    _support_cookie = None
    _kind = None
    _name = None
    _model = None
    _version = None
    _encoding = None
    is_dummy = False

    def __init__(self, support_cookie=None, kind=None, name=None, model=None, version=None, encoding=None):
        self._support_cookie = self._support_cookie or support_cookie
        self._kind = self._kind or kind
        self._name = self._name or name
        self._model = self._model or model
        self._version = self._version or version
        self._encoding = self._encoding or encoding

    @property
    def support_cookie(self):
        return self._support_cookie or False

    @property
    def kind(self):
        return self._kind or ''

    @property
    def name(self):
        return self._name or ''

    @property
    def model(self):
        return self._model or ''

    @property
    def version(self):
        return self._version or ''

    @property
    def encoding(self):
        return self._encoding or settings.DEFAULT_CHARSET

    def __hash__(self):
        guid = uuid.uuid5(uuid.NAMESPACE_DNS, "%s-%s-%s-%s-%s-%s" % (
                self.support_cookie,
                self.kind,
                self.name,
                self.model,
                self.version,
                self.encoding,
            ))
        return hash(str(guid))

    @classmethod
    def detect(cls, meta):
        raise NotImplementedError

    def non_cached_detect(self, meta):
        return self


class UserAgentRegexPatternDevice(Device):
    _patterns = None

    @classmethod
    def detect(cls, meta):
        user_agent = meta.get('HTTP_USER_AGENT', None)
        if not user_agent:
            return None

        for pattern in cls._patterns:
            name, pattern = pattern
            m = pattern.match(user_agent)
            if m:
                device = cls(name=name, **m.groupdict())
                return device
        return None

class DummyDevice(Device):
    is_dummy = True
    _support_cookie = True

