#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
from ..conf import settings
from ..core import detect

import e4u
e4u.load()

def _get_device(request):
    return getattr(request, 'device', detect(request.META))

class DeviceEmojiTranslationMiddleware(object):
    u"""Translate device emoji to unicode emoji middleware. DO NOT USE this with `mfw.middleware.encoding.DeviceEncodingMiddleware`."""
    def process_request(self, request):
        u"""Translate emoji encoding in GET and POST"""
        device = _get_device(request)
        
        if device.carrier is None:
            return
        
        def _convert_dict(d, profile):
            for k, v in d.iteritems():
                d[k] = e4u.translate(v, **profile)
                
        request.encoding = device.encoding
        profile = {'carrier': device.carrier, 'encoding': device.encoding}
        
        request.GET._mutable = True
        request.POST._mutable = True
        _convert_dict(request.GET, profile)
        _convert_dict(request.POST, profile)
        request.GET._mutable = False
        request.POST._mutable = False
    
    def process_response(self, request, response):
        u"""Translate emoji encoding in response"""
        device = _get_device(request)
        
        if response['content-type'].startswith('text/'):
            c = unicode(response.content, 'utf8')
            if device.carrier is None:
                profile = {
                    'carrier': settings.MFW_EMOJI_DEFAULT_CARRIER,
                    'encoding': settings.MFW_EMOJI_DEFAULT_ENCODING,
                }
            else:
                profile = {'carrier': device.carrier, 'encoding': device.encoding}
                response['content-type'] = 'application/xhtml+xml; charset=%s' % device.encoding
            c = e4u.translate(c, reverse=True, **profile)
            response.content = c.encode(profile['encoding'], 'replace')
        return response