# vim: set fileencoding=utf-8 :
"""
Mobilephone


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
from django.conf import settings
from mfw.device.base import Device


def appraisal(device, meta):
    """check carrier CIDR and add ``reliable`` attribute to device instance"""
    if settings.MFW_CHECK_DEVICE_RELIABLE:
        from IPy import IP
        from mfw.cidr import get_cidr
        cidr = get_cidr(device.carrier)
        remote_addr = meta.get('REMOTE_ADDR', None)
        if cidr and remote_addr and IP(remote_addr) in cidr:
            device._reliable = True
    device.__class__.reliable = property(lambda self: getattr(self, '_reliable', False))
    return device


class Mobilephone(Device):
    _kind = 'mobilephone'

    @property
    def carrier(self):
        return self._name.lower()

    @property
    def uid(self):
        return self._uid


class DoCoMo(Mobilephone):
    _name = 'DoCoMo'

    @classmethod
    def detect(cls, meta):
        pattern_mova = re.compile(r"DoCoMo/1.0/(?P<model>[^/]*)(?:/c(?P<cache>\d*)|)")
        pattern_foma = re.compile(r"DoCoMo/2.0 (?P<model>[^\(]*)\(c(?P<cache>\d*)")

        uid = meta.get('HTTP_X_DCMGUID', None)
        user_agent = meta.get('HTTP_USER_AGENT', None)
        if not user_agent:
            return None

        m = pattern_mova.match(user_agent)
        if not m:
            m = pattern_foma.match(user_agent)
        if not m:
            return None
        kwargs = m.groupdict()
        kwargs['cache'] = int(kwargs['cache']) if kwargs.get('cache', None) else 5

        # is this device support cookie?
        cache = kwargs.pop('cache')
        kwargs['support_cookie'] = cache >= 500

        instance = cls(**kwargs)
        instance._encoding = 'cp932'
        instance._uid = uid
        return appraisal(instance, meta)


class KDDI(Mobilephone):
    _name = 'KDDI'

    @classmethod
    def detect(cls, meta):
        pattern = re.compile(r"(?:(?:KDDI-)|(?:SIE-))(?P<model>[^\s/]*)")

        uid = meta.get('HTTP_X_UP_SUBNO', None)
        user_agent = meta.get('HTTP_USER_AGENT', None)
        if not user_agent:
            return None

        m = pattern.match(user_agent)
        if not m:
            return None
        kwargs = m.groupdict()

        kwargs['support_cookie'] = True

        instance = cls(**kwargs)
        instance._encoding = 'cp932'
        instance._uid = uid
        return appraisal(instance, meta)


class Softbank(Mobilephone):
    _name = 'Softbank'

    @classmethod
    def detect(cls, meta):
        pattern = re.compile(r"(?P<generation>J-PHONE|Vodafone|SoftBank)/(?P<version>[\d\.]*)/(?P<model>[^/\[]*)")

        uid = meta.get('HTTP_X_JPHONE_UID', None)
        user_agent = meta.get('HTTP_USER_AGENT', None)
        if not user_agent:
            return None

        m = pattern.match(user_agent)
        if not m:
            return None
        kwargs = m.groupdict()

        # is this device support cookie?
        generation = kwargs.pop('generation')
        version = kwargs.pop('version')
        if generation == 'J-PHONE':
            kwargs['support_cookie'] = version.startswith('5')
        else:
            kwargs['support_cookie'] = True

        instance = cls(**kwargs)
        instance._encoding = 'utf-8'
        instance._uid = uid
        return appraisal(instance, meta)
