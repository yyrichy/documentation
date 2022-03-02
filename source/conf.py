from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------

project = 'VapoR\'s Docs'
copyright = '2022, VapoR'
author = 'VapoR'

# The full version, including alpha/beta/rc tags
release = '2.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'recommonmark',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
]
autosectionlabel_prefix_document = True

html_theme = 'karma_sphinx_theme'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme_options = {
    'navigation_depth': 5,
    'includehidden': True,
    'titles_only': False
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../common/_static']

html_favicon = '../common/_static/img/logo.png'
html_title = "VapoR's Docs"
html_short_title = "VDocs"

def setup(app):
    app.add_config_value('recommonmark_config', {
            #'url_resolver': lambda url: github_doc_root + url,
            'enable_math': False,
            'enable_inline_math': False,
            'enable_eval_rst': True,
        }, True)
    app.add_transform(AutoStructify)
