# vim: set fileencoding=utf-8 :
"""
templatetags for using japanese emoji in template


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
import e4u
from django import template

register = template.Library()


class EmojiNode(template.Node):
    """Emoji template node"""
    def __init__(self, code):
        self.code = code.upper()

    def render(self, context):
        symbol = e4u.get(self.code)
        return unicode(symbol.unicode)
    

@register.tag
def emoji(parser, token):
    """Insert emoji via emoji id
    
    Usage:
        {% emoji 'emoji_id' %}
    """
    bits = token.split_contents()

    if len(bits) == 2:
        return EmojiNode(bits[1][1:-1])
    else:
        raise template.TemplateSyntaxError("%r tag require a argument" % bits[0])
