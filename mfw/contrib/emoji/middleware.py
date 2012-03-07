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
from django.utils.encoding import force_unicode

import e4u

def translate(src, carrier, encoding):
    c = force_unicode(src)
    # translate all emoji
    c = e4u.translate(c, reverse=True, **{'carrier': carrier, 'encoding': encoding})
    return c

def encode(src, encoding):
    c = force_unicode(src)
    # insted of raise exception, replace character which cannot encode.
    dst = c.encode(encoding, 'replace')
    return dst

def translate_dict(src, carrier):
    src._mutable = True
    for key, value in src.iteritems():
        src[key] = e4u.translate(value, **{'carrier': carrier, 'encoding': settings.DEFAULT_CHARSET})
    src._mutable = False
    src._mfw_encoded = True


class DeviceEmojiTranslationMiddleware(object):
    """Translate device emoji to unicode emoji. DO NOT USE this with `mfw.middleware.encoding.DeviceEncodingMiddleware`."""
    def process_request(self, request):
        # tell django to use device encoding
        if not hasattr(request.device, 'carrier'):
            return

        # translate GET/POST
        if not getattr(request.GET, '_mfw_translated', False):
            translate_dict(request.GET, request.device.carrier)
        if not getattr(request.POST, '_mfw_translated', False):
            translate_dict(request.POST, request.device.carrier)
    
    def process_response(self, request, response):
        if response['content-type'].startswith('text/'):
            if not getattr(response, '_mfw_translated', False):
                if not hasattr(request.device, 'carrier'):
                    carrier = settings.MFW_EMOJI_DEFAULT_CARRIER
                else:
                    carrier = request.device.carrier
                encoding = request.device.encoding
                response.content = translate(response.content, carrier, encoding)
                response._mfw_translated = True

        return response
