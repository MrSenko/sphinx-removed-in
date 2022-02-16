import os
import sys
import pytest


PARENT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, PARENT)


@pytest.mark.sphinx(buildername='html', srcdir=os.path.join(PARENT, 'docs'))
def test_sphinx_build(app, status, warning):
    app.build()
    html = (app.outdir / 'index.html').read_text()

    assert 'Removed in version 1.2' in html
    assert 'Removed in version 3.2' in html
