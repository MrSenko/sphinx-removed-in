#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = __import__('sphinx_removed_in').__version__

with open('README.rst') as file:
    long_description = file.read()

config = {
    'name': 'sphinx-removed-in',
    'version': __version__,
    'packages': find_packages(exclude=['tests']),
    'author': 'Alexander Todorov',
    'author_email': 'atodorov@MrSenko.com',
    'license': 'BSD',
    'description': 'versionremoved and removed-in directives for Sphinx',
    'long_description': long_description,
    'url': 'https://github.com/MrSenko/sphinx-removed-in',
    'keywords': ['Sphinx'],
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    'zip_safe': False,
    'install_requires': ['Sphinx'],
}

setup(**config)
