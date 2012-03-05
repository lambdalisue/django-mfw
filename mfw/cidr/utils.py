# vim: set fileencoding=utf-8 :
"""
CIDR loader


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
from mfw.cidr.scrapers import CIDRScraper
from mfw.models import DatabaseCIDR

try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module


def get_scraper(path=None):
    """
    Return an instance of a cidr scraper, given the dotted
    Python import path (as a string) to the cidr scraper class.

    If the cidr scraper cannot be located (e.g., because no such module
    exists, or because the module does not contain a class of the
    appropriate name), ``django.core.exceptions.ImproperlyConfigured``
    is raised.
    
    """
    i = path.rfind('.')
    module, attr = path[:i], path[i+1:]
    try:
        mod = import_module(module)
    except ImportError, e:
        raise ImproperlyConfigured('Error loading mfw cidr %s: "%s"' % (module, e))
    try:
        cls = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured('Module "%s" does not define a mfw cidr named "%s"' % (module, attr))
    if cls and not issubclass(cls, CIDRScraper):
        raise ImproperlyConfigured('CIDR scraper class "%s" must be a subclass of ``mfw.cidr.scrapers.CIDRScraper``' % path)
    return cls()


def get_cidr(carrier):
    cidr, created = DatabaseCIDR.objects.get_or_create(
            carrier=carrier
        )

    if created or cidr.is_expired:
        scraper = get_scraper(settings.MFW_CIDR_SCRAPER_CLASSES[carrier])
        cidr.data = scraper.scrape()
        cidr.save()

    return cidr
