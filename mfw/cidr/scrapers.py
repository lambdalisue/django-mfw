# vim: set fileencoding=utf-8 :
"""
short module explanation


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
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

ADDR = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
MASK = r"/\d{1,3}"
addr_and_mask_r = re.compile(ADDR+MASK)
addr_r = re.compile(ADDR)
mask_r = re.compile(MASK)

class CIDRScraper(object):
    carrier = None
    url = None

    def scrape(self):
        raise NotImplementedError

class DoCoMoCIDRScraper(CIDRScraper):
    carrier = 'docomo'
    url = r"http://www.nttdocomo.co.jp/service/developer/make/content/ip/index.html"

    def scrape(self):
        soup = BeautifulSoup(urlopen(self.url).read())
        soup = soup.findAll("li", text=addr_and_mask_r)
        return list(soup)

class KDDICIDRScraper(CIDRScraper):
    carrier = 'kddi'
    url = r"http://www.au.kddi.com/ezfactory/tec/spec/ezsava_ip.html"

    def scrape(self):
        soup = BeautifulSoup(urlopen(self.url).read())
        soup = soup.findAll("div", "TableText")
        data = []
        i = 0
        while i < len(soup):
            addr = soup[i]
            if addr.string is None or addr.find('s') != None or not addr_r.match(addr.string):
                i += 1
                continue
            mask = soup[i+1]
            data.append(addr.string + mask.string)
            i += 2
        return data

class SoftbankCIDRScraper(CIDRScraper):
    carrier = 'softbank'
    url = r"http://creation.mb.softbank.jp/mc/tech/tech_web/web_ipaddress.html"

    def scrape(self):
        soup = BeautifulSoup(urlopen(self.url).read())
        soup = soup.findAll("th", text=addr_and_mask_r)
        return list(soup)
