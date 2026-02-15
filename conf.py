# Configuration file for the Sphinx documentation builder.

project = 'Whoo API'
copyright = '2026, Whoo API Documentation'
author = 'API Documentation Team'
release = '1.0'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# Theme
html_theme = 'sphinx_rtd_theme'

# Paths
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML output options
html_static_path = ['_static']
html_theme_options = {
    'navigation_depth': 4,
    'titles_only': False
}

# Language
language = 'ja'
