#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

from ..core import detect

_thread_locals = local()
def get_flavour():
    return getattr(_thread_locals, 'flavour', None)

def _get_device(request):
    device = getattr(request, 'device', detect(request.META))
    return device

class DeviceFlavourDetectionMiddleware(object):
    u"""Detect device flavour via `uamd` library and set to `request.flavour`"""
    def process_request(self, request):
        device = _get_device(request)
        
        module_name = device.__module__.split('.')[-1]
        class_name = device.__class__.__name__
        model = device.model or u""
        version = device.version or u""
        
        flavour = [module_name, class_name, model, version]
        flavour = [x.lower() for x in flavour if x]
        flavour = u"/".join(flavour)
        
        request.flavour = flavour
        _thread_locals.flavour = flavour