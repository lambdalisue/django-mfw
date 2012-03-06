# vim: set fileencoding=utf-8 :
"""
Japanese Emoji translation middleware


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
from django.conf import settings

import e4u


class DeviceEmojiTranslationMiddleware(object):
    """Translate device emoji to unicode emoji. DO NOT USE this with `mfw.middleware.encoding.DeviceEncodingMiddleware`."""
    def process_request(self, request):
        """Translate emoji encoding in GET and POST"""
        
        if not hasattr(request.device, 'carrier'):
            return
        
        def _convert_dict(d, profile):
            for k, v in d.iteritems():
                d[k] = e4u.translate(v, **profile)
                
        profile = {'carrier': request.device.carrier, 'encoding': request.device.encoding}
        
        request.GET._mutable = True
        request.POST._mutable = True
        _convert_dict(request.GET, profile)
        _convert_dict(request.POST, profile)
        request.GET._mutable = False
        request.POST._mutable = False
    
    def process_response(self, request, response):
        """Translate emoji encoding in response"""
        
        if response['content-type'].startswith('text/'):
            c = unicode(response.content, 'utf-8')
            if not hasattr(request.device, 'carrier'):
                profile = {
                    'carrier': settings.MFW_EMOJI_DEFAULT_CARRIER,
                    'encoding': settings.MFW_EMOJI_DEFAULT_ENCODING,
                }
            else:
                profile = {'carrier': request.device.carrier, 'encoding': request.device.encoding}
                response['content-type'] = 'application/xhtml+xml; charset=%s' % request.device.encoding
            c = e4u.translate(c, reverse=True, **profile)
            response.content = c.encode(profile['encoding'], 'replace')
        return response
