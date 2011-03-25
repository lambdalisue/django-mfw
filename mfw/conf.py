#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
from django.conf import settings as django_settings

class SettingsProxy(object):
    def __init__(self, settings, defaults):
        self.settings = settings
        self.defaults = defaults

    def __getattr__(self, attr):
        try:
            return getattr(self.settings, attr)
        except AttributeError:
            try:
                return getattr(self.defaults, attr)
            except AttributeError:
                raise AttributeError, u'settings object has no attribute "%s"' % attr

class defaults(object):
    # emoji
    #--------------------------------------------------------------------
    MFW_EMOJI_DEFAULT_CARRIER = 'kddi_img'
    MFW_EMOJI_DEFAULT_ENCODING = 'utf8'
    # flavours
    #--------------------------------------------------------------------
    MFW_FLAVOURS_TEMPLATE_PREFIX = u''
    MFW_FLAVOURS_TEMPLATE_LOADERS = []
    for loader in django_settings.TEMPLATE_LOADERS:
        if loader != 'mfw.template.loaders.flavour.Loader':
            MFW_FLAVOURS_TEMPLATE_LOADERS.append(loader)
    MFW_FLAVOURS_TEMPLATE_LOADERS = tuple(MFW_FLAVOURS_TEMPLATE_LOADERS)

settings = SettingsProxy(django_settings, defaults)

