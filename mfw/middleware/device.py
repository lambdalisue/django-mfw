#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
from ..core import detect

class DeviceDetectionMiddleware(object):
    u"""Detect device via HTTP META using `uamd` library and store it in `request`"""
    def process_request(self, request):
        device = detect(request.META)
        request.device = device