from sphinx.locale import versionlabels
from sphinx.directives.other import VersionChange


__version__ = '0.1.0'


def setup(app):
    for _directive in ['versionremoved', 'removed-in']:
        if _directive not in versionlabels:
            versionlabels[_directive] = 'Removed in version %s'
            app.add_directive(_directive, VersionChange)

    return {'version': __version__}
