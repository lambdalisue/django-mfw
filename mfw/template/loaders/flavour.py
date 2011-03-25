#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
from django.template import TemplateDoesNotExist
from django.template.loader import find_template_loader, BaseLoader

from ...conf import settings
from ...middleware.flavour import get_flavour

class Loader(BaseLoader):
    is_usable = True

    def __init__(self, *args, **kwargs):
        loaders = []
        for loader_name in settings.MFW_FLAVOURS_TEMPLATE_LOADERS:
            loader = find_template_loader(loader_name)
            if loader is not None:
                loaders.append(loader)
        self.template_source_loaders = tuple(loaders)
        super(BaseLoader, self).__init__(*args, **kwargs)

    def sliceup_flavour_name(self, flavour):
        offset = flavour.rfind(u'/')
        if offset != -1:
            return flavour[:offset]
        else:
            return None
    def prepare_template_name(self, template_name, flavour):
        template_name = u'%s/%s' % (flavour, template_name)
        if settings.MFW_FLAVOURS_TEMPLATE_PREFIX:
            template_name = settings.MFW_FLAVOURS_TEMPLATE_PREFIX + template_name
        return template_name

    def load_template(self, template_name, template_dirs=None):
        tried = []
        flavour = get_flavour()
        while(flavour):
            _template_name = self.prepare_template_name(template_name, flavour)
            for loader in self.template_source_loaders:
                try:
                    return loader(_template_name, template_dirs)
                except TemplateDoesNotExist:
                    pass
            tried.append(_template_name)
            # slice up flavour
            flavour = self.sliceup_flavour_name(flavour)
        raise TemplateDoesNotExist("Tried %s" % tried)

    def load_template_source(self, template_name, template_dirs=None):
        tried = []
        flavour = get_flavour()
        while(flavour):
            _template_name = self.prepare_template_name(template_name, flavour)
            for loader in self.template_source_loaders:
                if hasattr(loader, 'load_template_source'):
                    try:
                        return loader.load_template_source(_template_name, template_dirs)
                    except TemplateDoesNotExist:
                        pass
            tried.append(_template_name)
            # slice up flavour
            flavour = self.sliceup_flavour_name(flavour)
        raise TemplateDoesNotExist("Tried %s" % tried)
