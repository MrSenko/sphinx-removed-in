__version__ = '0.2.1'


def setup(app):
    try:
        from sphinx.domains.changeset import versionlabels
    except ImportError:
        from sphinx.locale import versionlabels
    from sphinx.directives.other import VersionChange

    try:
        from sphinx.domains.changeset import versionlabel_classes
    except ImportError:
        versionlabel_classes = {}  # dummy dict for Sphinx < 2

    for _directive in ['versionremoved', 'removed-in']:
        if _directive not in versionlabels:
            versionlabels[_directive] = 'Removed in version %s'
            versionlabel_classes[_directive] = 'removed'
            app.add_directive(_directive, VersionChange)

    return {'version': __version__}
