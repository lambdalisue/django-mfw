# vim: set fileencoding=utf-8 :
from setuptools import setup, find_packages

version = "0.4.0"

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name="django-mfw",
    version=version,
    description = "Django framework for mobilephone/smartphone site",
    long_description=read('README.rst'),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = "django mobile smartphone emoji device detection dynamic template",
    author = "Alisue",
    author_email = "lambdalisue@hashnote.net",
    url=r"https://github.com/lambdalisue/django-mfw",
    download_url = r"https://github.com/lambdalisue/django-mfw/tarball/master",
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires=[
        'django>=1.3',
        'distribute',
        'setuptools-git',
        'IPy',
        'BeautifulSoup',
        'e4u',
    ],
    test_suite='runtests.runtests',
    tests_require=[
        'PyYAML',
        'django-jenkins',
    ],
)
