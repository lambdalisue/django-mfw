# vim: set fileencoding=utf-8 :
"""
Unittest module of ...


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
import re
from django.test import TestCase
from mfw.cidr.scrapers import DoCoMoCIDRScraper
from mfw.cidr.scrapers import KDDICIDRScraper
from mfw.cidr.scrapers import SoftbankCIDRScraper

addr_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,3}")

class MFWCIDRScraperTestCase(TestCase):

    def test_docomo_cidr_scraper(self):
        data = DoCoMoCIDRScraper().scrape()
        self.assertTrue(isinstance(data, list))
        self.assertTrue(len(data) > 0)
        self.assertTrue(addr_pattern.match(data[0]))

    def test_kddi_cidr_scraper(self):
        data = KDDICIDRScraper().scrape()
        self.assertTrue(isinstance(data, list))
        self.assertTrue(len(data) > 0)
        self.assertTrue(addr_pattern.match(data[0]))

    def test_softbank_cidr_scraper(self):
        data = SoftbankCIDRScraper().scrape()
        self.assertTrue(isinstance(data, list))
        self.assertTrue(len(data) > 0)
        self.assertTrue(addr_pattern.match(data[0]))

