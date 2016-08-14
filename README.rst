Sphinx Removed In Extension
---------------------------

.. image:: https://travis-ci.org/MrSenko/sphinx-removed-in.svg?branch=master
   :target: https://travis-ci.org/MrSenko/sphinx-removed-in

.. image:: https://coveralls.io/repos/github/MrSenko/sphinx-removed-in/badge.svg?branch=master
   :target: https://coveralls.io/github/MrSenko/sphinx-removed-in?branch=master

.. image:: https://landscape.io/github/MrSenko/sphinx-removed-in/master/landscape.svg?style=flat
   :target: https://landscape.io/github/MrSenko/sphinx-removed-in/master
   :alt: Code Health

This is a Sphinx extension which recognizes the ``.. versionremoved::`` and
``.. removed-in::`` directives. These are missing from Sphinx'es
`core markup <http://www.sphinx-doc.org/en/stable/markup/para.html>`_.

Installation
============

Use pip to install from PyPI:

::

    pip install sphinx-removed-in


Configure your ``conf.py``:

::

    # Add any Sphinx extension module names here, as strings. They can be extensions
    # coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
    extensions = ['sphinx_removed_in']

Contributing
============

Source code and issue tracker are at https://github.com/MrSenko/sphinx-removed-in
