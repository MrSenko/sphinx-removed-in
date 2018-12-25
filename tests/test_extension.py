import os
import sys
import unittest
from sphinx_testing import with_app


sys.path.insert(0,
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


class TestExtension(unittest.TestCase):
    @with_app(buildername='html', srcdir='./docs', copy_srcdir_to_tmpdir=True)
    def test_sphinx_build(self, app, status, warning):
        app.build()
        html = (app.outdir / 'index.html').read_text()

        self.assertIn('Removed in version 1.2', html)
        self.assertIn('Removed in version 3.2', html)


if __name__ == "__main__":
    unittest.main()
