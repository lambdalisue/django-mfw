# vim: set fileencoding=utf-8 :
"""
Device loader


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
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from mfw.device.base import Device
from mfw.device.base import DummyDevice

try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module


def get_device_class(path=None):
    """
    Return an class of a device, given the dotted
    Python import path (as a string) to the device class.

    If the device cannot be located (e.g., because no such module
    exists, or because the module does not contain a class of the
    appropriate name), ``django.core.exceptions.ImproperlyConfigured``
    is raised.
    
    """
    i = path.rfind('.')
    module, attr = path[:i], path[i+1:]
    try:
        mod = import_module(module)
    except ImportError, e:
        raise ImproperlyConfigured('Error loading mfw device %s: "%s"' % (module, e))
    try:
        cls = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured('Module "%s" does not define a mfw device named "%s"' % (module, attr))
    if cls and not issubclass(cls, Device):
        raise ImproperlyConfigured('Device class "%s" must be a subclass of ``mfw.device.base.Device``' % path)
    return cls


class DeviceDetector(object):
    def __init__(self):
        self._device_classes = []
        for device_class in settings.MFW_DEVICE_CLASSES:
            self._device_classes.append(get_device_class(device_class))
        self._device_cache = {}

    def detect(self, meta):
        device = self._cached_detect(meta)
        device = self._non_cached_detect(device, meta)
        return device

    def _cached_detect(self, meta):
        user_agent = meta.get('HTTP_USER_AGENT', None)
        # does the request has HTTP_USER_AGENT?
        if not user_agent:
            return DummyDevice()
        # Try to find Device instance from cache
        if user_agent in self._device_cache:
            return self._device_cache[user_agent]
        # Try to detect the Device
        for device_class in self._device_classes:
            device = device_class.detect(meta)
            if device:
                self._device_cache[user_agent] = device
                return device
        # No suite device found
        return DummyDevice()

    def _non_cached_detect(self, device, meta):
        # Call non cached detect
        device = device.non_cached_detect(meta)
        return device

