#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Morten Amundsen'
__contact__ = 'm.amundsen@sportradar.com'

from setuptools import find_packages, setup

version = '0.2.0'
long_desc = '''emailyzer -- a parser from .eml and .msg email files
with a focus extracting features relevant for email analysis.
'''.lstrip()

classifiers = [
    'Development Status :: 3 - Alpha',
    'Topic :: Communications :: Email',
    'Intended Audience :: Sportradar, NTNU',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Topic :: Text Processing',
]

requires = [
    'beautifulsoup4',
    'lxml',
    'mail-parser',
    'extract-msg'
]

setup(
    name='emailyzer',
    version=version,
    description='A parser for .eml and .msg email files',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    install_requires=requires,
    url='https://github.com/mortea15/emailyzer.git',
    author=__author__,
    author_email=__contact__,
    packages=['emailyzer', 'emailyzer.classes', 'emailyzer.helpers', 'emailyzer.tests'], #find_packages(),
    classifiers=classifiers,
    zip_safe=False,
    entry_points={'console_scripts': ['emailyzer = emailyzer.__main__:main']}
)
