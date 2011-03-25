#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
from datetime import datetime
from dateutils import relativedelta
from IPy import IP

import uamd

from ..models import CIDRCache

class DatabaseLoader(uamd.cidr.Loader):
    u"""Loading cidr via carrier from Django's Database and Internet"""
    _EXPIRE = relativedelta(weeks=1)
    _DELIMITER = u"\n"
    
    def _str_to_data(self, s):
        values = s.split(self._DELIMITER)
        return map(lambda x: IP(x), values)
    def _data_to_str(self, d):
        values = map(lambda x: unicode(x), d)
        return self._DELIMITER.join(values)
    
    def get(self, carrier):
        expire = datetime.now() - self._EXPIRE
        cache = getattr(self, '_data_cache', None)
        if cache and cache[0] > expire:
            return cache[1]
        try:
            cidr = CIDRCache.objects.get(updated_at__gt=expire, carrier=carrier)
        except CIDRCache.DoesNotExist:
            cidr = CIDRCache.objects.get_or_create(carrier=carrier)[0]
            cidr.data = self._data_to_str(self.fetch(carrier))
            cidr.save()
        data = self._str_to_data(cidr.data)
        updated_at = datetime.now()
        setattr(self, '_data_cache', (updated_at, data))
        return data
database_loader = DatabaseLoader()