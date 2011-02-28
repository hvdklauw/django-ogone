#!/usr/bin/env python

from setuptools import setup, find_packages

try:
    README = open('README.md').read()
except:
    README = None

try: 
    LICENSE = open('LICENSE.txt').read() 
except: 
    LICENSE = None

setup(
    name = 'django-ogone',
    version = '0.1',
    description='Python/Django client to the ogone payment system.',
    long_description=README,
    author = 'Thierry Schellenbach',
    author_email = 'thierryschellenbach at googles great mail service',
    license = LICENSE,
    url = 'http://github.com/tschellenbach/Django-ogone',
    packages = find_packages(exclude=['examples']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
    ],
)
