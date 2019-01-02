__version__ = '0.1.3'


def setup(app):
    from sphinx.domains.changeset import versionlabels
    from sphinx.directives.other import VersionChange

    for _directive in ['versionremoved', 'removed-in']:
        if _directive not in versionlabels:
            versionlabels[_directive] = 'Removed in version %s'
            app.add_directive(_directive, VersionChange)

    return {'version': __version__}
