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
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    'myst_parser'
]
autosectionlabel_prefix_document = True
myst_heading_anchors = 5

html_theme = 'sphinx_book_theme'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme_options = {
    'use_download_button': False,
    'logo_only': True,
    'show_toc_level': 2,
    'home_page_in_toc': True,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['../common/_static']

html_favicon = '../common/_static/img/logo.png'
html_logo = '../common/_static/img/cloud-circle.png'
html_title = 'VapoR\'s Docs'
html_short_title = 'VDocs'

def setup(app):
    app.add_config_value('recommonmark_config', {
            #'url_resolver': lambda url: github_doc_root + url,
            'enable_math': False,
            'enable_inline_math': False,
            'enable_eval_rst': True,
        }, True)
    app.add_transform(AutoStructify)
