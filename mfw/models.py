# vim: set fileencoding=utf-8 :
"""
Database CIDR


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
from datetime import timedelta
from IPy import IP
from django.conf import settings
from django.db import models
from django.utils.text import ugettext_lazy as _

try:
    from django.utils.timezone import now
except ImportError:
    from datetime import datetime
    now = datetime.now


class DatabaseCIDR(models.Model):
    carrier = models.CharField(_('carrier'), max_length=50, unique=True)
    _data = models.TextField(_('data'), db_column='data', blank=True)
    updated_at = models.DateTimeField(_('last updated'), auto_now=True)

    class Meta:
        verbose_name = _('cidr')
        verbose_name_plural = _('cidrs')

    @property
    def data(self):
        if hasattr(self, '_data_cache'):
            return self._data_cache
        self._data_cache = [IP(x) for x in self._data.split("\n")]
        return self._data_cache

    @data.setter
    def data(self, value):
        if hasattr(self, '_data_cache'):
            del self._data_cache
        self._data = "\n".join(value)

    @property
    def is_expired(self):
        return self.updated_at > now() + timedelta(days=settings.MFW_CIDR_EXPIRATION_DAYS)

    def __unicode__(self):
        return "CIDR of %s" % self.carrier

    def __iter__(self):
        return self.data.__iter__()

    def __contains__(self, x):
        for address in self.data:
            if x in address:
                return True
        return False

