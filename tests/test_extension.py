import os
import sys
import pytest


PARENT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, PARENT)


@pytest.mark.sphinx(buildername='html', srcdir=os.path.join(PARENT, 'docs'))
def test_sphinx_build(app, status, warning):
    app.build()
    try:
        html = (app.outdir / 'index.html').read_text()
    except AttributeError:
        # an older version of sphinx (used e.g. on Python 2)
        # use the now deprecated API instead
        html = (app.outdir / 'index.html').text()

    assert 'Removed in version 1.2' in html
    assert 'Removed in version 3.2' in html
