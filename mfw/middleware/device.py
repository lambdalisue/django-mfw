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
        request.device = lambda : None
        request.device.encoding = 'utf-8'
        request.device.carrier = 'softbank'
        request.device.support_cookie = False
        request.device.model = ""
        request.device.version = None
        request.device.spoof = False
        request.device.uid = 10
