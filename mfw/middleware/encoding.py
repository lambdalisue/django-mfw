#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
from ..core import detect

def _get_device(request):
    return getattr(request, 'device', detect(request.META))

class DeviceEncodingMiddleware(object):
    u"""Encoding response via device middleware. DO NOT USE this with `mfw.middleware.emoji.EmojiTranslationMiddleware`"""
    def process_response(self, request, response):
        u"""Convert encoding in response"""
        device = _get_device(request)
        
        if response['content-type'].startswith('text/'):
            if device.encoding is not None:
                c = unicode(response.content, 'utf8')
                response.content = c.encode(device.encoding, 'replace')
                response['content-type'] = 'application/xhtml+xml; charset=%s' % device.encoding
        return response