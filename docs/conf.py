import sys
import os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

CURDIR = os.path.abspath(os.path.dirname(__file__))

local_plantuml_path = os.path.join(os.path.dirname(__file__), "_utility", "plantuml-1.2023.6.jar")
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"

extensions = [
    'sphinx_rtd_theme',
    'hoverxref.extension',
    'sphinxemoji.sphinxemoji',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.contentui',
    'sphinxcontrib.httpdomain',
#    'sphinxcontrib.images',
    'sphinxcontrib.plantuml',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.graphviz',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'sphinx_search.extension',
    'sphinx_tabs.tabs',
    ]

bibtex_bibfiles = [
    'reference-1-book-food-method.bib',
    'reference-2-article-food-method.bib',
    'reference-3-book-food-ref.bib',
    'reference-4-article-food-ref.bib',
    'reference-5-misc-ontology.bib',
    'reference-6-misc-data.bib',
    'reference-7-misc-web.bib',
    'reference-8-article-technology.bib',
]

hoverxref_auto_ref = True
hoverxref_domains = ["py"]
hoverxref_roles = [
    "option",
    # Documentation pages
    # Not supported yet: https://github.com/readthedocs/sphinx-hoverxref/issues/18
    "doc",
    # Glossary terms
    "term",
]
hoverxref_role_types = {
    "mod": "modal",        # for Python Sphinx Domain
    "doc": "modal",        # for whole docs
    "class": "tooltip",    # for Python Sphinx Domain
    "ref": "tooltip",      # for hoverxref_auto_ref config
    "confval": "tooltip",  # for custom object
    "term": "tooltip",     # for glossaries
}

# -- MathJax configuration ----------------------------------
# new link fails
#mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/latest.min.js'

# current path is shutting down
mathjax_path = 'https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

# -- GraphViz configuration ----------------------------------
graphviz_output_format = 'svg'

# -- sphinxemoji configuration -------------------------------
sphinxemoji_style = 'twemoji'

templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
project = 'Sphinx Catalog'
copyright = '2023, Ontomatica'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the built documents.
# The short X.Y version.
version = '0.1'

# The full version, including alpha/beta/rc tags.
release = 'a'

# Turns on numbered figures for HTML output
number_figures = True


# -- Bibliography configuration -----------------------------
# see https://wnielson.bitbucket.org/projects/sphinx-natbib/
natbib = {
    'file': 'reference-1-book-food-method.bib,reference-2-article-food-method.bib,reference-3-book-food-ref.bib,reference-4-article-food-ref.bib,reference-5-misc-ontology.bib,reference-6-misc-data.bib,reference-7-misc-web.bib,reference-8-article-technology.bib',
    'brackets': '[]',
    'separator': ',',
    'style': 'numbers',
    'sort': True,
}

# There are two options for replacing |today|: either, you set today to some non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.

today_fmt = '%y-%m-%d'


# The reST default role (used for this markup: `text`) to use for all documents.
default_role = None

# make rst_epilog a variable, so you can add other epilog parts to it
rst_epilog =""

pygments_style = 'sphinx'
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
# Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 9,
    'includehidden': True,
    'titles_only': False,
    'body_max_width': 'none'
}

html_title = ""
html_short_title = 'TOCTREE'

# The name of an image file (relative to this directory) to place at the top of the sidebar.
#html_logo = 'Ontomatica.png'


html_static_path = [
    '_image',
    '_static',
    '_substitution',
]

# These paths are either relative to html_static_path or fully qualified paths (eg. https://...)

# Add any extra paths that contain custom files (such as robots.txt or .htaccess) here, relative to this directory.
# These files are copied directly to the root of the documentation.
#html_extra_path = ['_images']

html_last_updated_fmt = '%y-%m-%d'
html_domain_indices = True
html_use_index = True
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
html_file_suffix = '.html'
html_search_language = 'en'
htmlhelp_basename = 'spx1'

