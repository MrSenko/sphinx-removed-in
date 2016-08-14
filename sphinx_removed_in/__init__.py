from .version import __version__
from sphinx.locale import versionlabels
from sphinx.directives.other import VersionChange


def setup(app):
    _directive = 'versionremoved'

    if _directive in versionlabels:
        return {'version': __version__}

    versionlabels[_directive] = 'Removed in version %s'
    app.add_directive(_directive, VersionChange)

    return {'version': __version__}
