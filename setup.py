#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author:        alisue
# date:            2011/03/22
#
from setuptools import setup, find_packages

version = "0.1rc2"

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
        name="django-mfw",
        version=version,
        description = "Django's Mobile Framework",
        long_description=read('README.rst'),
        classifiers = [
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP',
        ],
        keywords = "django mobile emoji device detection dynamic template",
        author = "Alisue",
        author_email = "lambdalisue@hashnote.net",
        url=r"https://github.com/lambdalisue/django-mfw",
        download_url = r"https://github.com/lambdalisue/django-mfw/tarball/master",
        license = 'BSD',
        packages = find_packages(),
        #include_package_data = True,
        zip_safe = True,
        install_requires=['setuptools', 'e4u', 'uamd'],
)

