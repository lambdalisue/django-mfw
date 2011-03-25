#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/24
#
from django import template

import e4u
e4u.load()

register = template.Library()

class EmojiNode(template.Node):
    def __init__(self, code):
        self.code = code.upper()

    def render(self, context):
        request = context.get('request', None)
        if request is None:
            raise AttributeError(u"'django.core.context_processors.request' is required to add to `TEMPLATE_CONTEXT_PROCESSORS`.")
        symbol = e4u.get(self.code)
        return unicode(symbol.unicode)
    
@register.tag
def emoji(parser, token):
    u"""Insert emoji via emoji id
    
    Usage:
        {% emoji 'emoji_id' %}
    """
    bits = token.split_contents()

    if len(bits) == 2:
        return EmojiNode(bits[1][1:-1])
    else:
        raise template.TemplateSyntaxError("%r tag require a argument" % bits[0])
