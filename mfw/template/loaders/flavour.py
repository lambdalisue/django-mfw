# vim: set fileencoding=utf-8 :
"""
Flavour template loader


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
from django.template import TemplateDoesNotExist
from django.template.loader import BaseLoader
from django.template.loader import find_template_loader

from mfw.middleware.flavour import get_flavour

class Loader(BaseLoader):
    """Flavour template loader"""
    is_usable = True

    def __init__(self, *args, **kwargs):
        loaders = []
        for loader_name in settings.TEMPLATE_LOADERS:
            if loader_name == 'mfw.template.loaders.flavour.Loader':
                continue
            loader = find_template_loader(loader_name)
            if loader is not None:
                loaders.append(loader)
        self.template_source_loaders = tuple(loaders)
        super(Loader, self).__init__(*args, **kwargs)

    def sliceup_flavour_name(self, flavour):
        offset = flavour.rfind(u'/')
        if offset != -1:
            return flavour[:offset]
        else:
            return None

    def prepare_template_name(self, template_name, flavour):
        template_name = u'%s/%s' % (flavour, template_name)
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
