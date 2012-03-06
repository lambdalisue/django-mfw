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
from django.test import TestCase
from django.template import TemplateDoesNotExist
from mfw.tests.mock import Mock
from mfw.tests.override_settings import override_settings
from mfw.template.loaders.flavour import Loader

class MockTemplateLoader(Mock):
    def load_template(self, template_name, template_dirs=None):
        raise TemplateDoesNotExist

    def load_template_source(self, template_name, template_dirs=None):
        raise TemplateDoesNotExist

@override_settings(TEMPLATE_LOADERS=(
        'mfw.template.loaders.flavour.Loader',
        'mfw.tests.test_template.test_flavour.MockTemplateLoader',
    ))
class MFWFlavourTemplateLoaderTestCase(TestCase):
    
    def test_load_template(self):
        loader = Loader()
        loader.get_flavour = Mock(return_value='browser/firefox/windows/1.0')
        
        template_name = 'test_template_name.html'

        try:
            loader.load_template(template_name)
        except TemplateDoesNotExist, e:
            # convert string message to list
            result = str(e).replace('Tried ', '')
            result = result.replace("u'", "").replace("'", "")
            result = result[1:-1]
            result = map(lambda x: x.strip(), result.split(','))
            expected = [
                    'browser/firefox/windows/1.0/test_template_name.html',
                    'browser/firefox/windows/test_template_name.html',
                    'browser/firefox/test_template_name.html',
                    'browser/test_template_name.html',
                    'test_template_name.html',
                ]
            # DO NOT USE assertItemsEqual because the order is also the matter
            self.assertEqual(result, expected)

    def test_load_template_source(self):
        loader = Loader()
        loader.get_flavour = Mock(return_value='browser/firefox/windows/1.0')
        
        template_name = 'test_template_name.html'

        try:
            loader.load_template_source(template_name)
        except TemplateDoesNotExist, e:
            # convert string message to list
            result = str(e).replace('Tried ', '')
            result = result.replace("u'", "").replace("'", "")
            result = result[1:-1]
            result = map(lambda x: x.strip(), result.split(','))
            expected = [
                    'browser/firefox/windows/1.0/test_template_name.html',
                    'browser/firefox/windows/test_template_name.html',
                    'browser/firefox/test_template_name.html',
                    'browser/test_template_name.html',
                    'test_template_name.html',
                ]
            # DO NOT USE assertItemsEqual because the order is also the matter
            self.assertEqual(result, expected)

