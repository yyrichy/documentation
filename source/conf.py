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
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
]
todo_include_todos = True
todo_emit_warnings = True
autosectionlabel_prefix_document = True

html_theme = 'furo'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme_options = {
    'sidebar_hide_name': True,
    'navigation_with_keys': True,
    'announcement': '<em>This site is a work in progress.</em>',
    'light_logo': 'img/cloud-circle.png',
    'dark_logo': 'img/cloud-circle.png',
    'light_css_variables': {
        'color-brand-primary': '#3864ED',
        'color-brand-content': '#0997C1',
        'color-admonition-background': '#F7F7F7'
    },
    'dark_css_variables': {
        'color-brand-primary': '#3864ED',
        'color-brand-content': '#2AE1FF',
        'color-admonition-background': '#383838'
    }
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
