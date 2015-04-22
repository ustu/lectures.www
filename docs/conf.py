# -*- coding: utf-8 -*-
#
# Основы Веб-программирования documentation build configuration file,
# created by sphinx-quickstart on Sun Jan 18 19:36:48 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os

import docutils
from docutils.parsers.rst import directives
from docutils.parsers.rst.roles import set_classes
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.builders.latex import LaTeXBuilder
from sphinx.directives.code import CodeBlock

directives.register_directive('no-code-block', CodeBlock)

# IMAGES
image_types = ['image/png', 'image/svg+xml', 'image/gif', 'image/jpeg']

# Redefine supported_image_types for the HTML and LaTeX builder
LaTeXBuilder.supported_image_types = image_types
StandaloneHTMLBuilder.supported_image_types = image_types

_LOGO = '_static/info-small.png'

html_logo = _LOGO
html_favicon = '_static/urfu.ico'
html_sidebars = {
    '**': ['globaltoc.html',
           'searchbox.html',
           'sourcelink.html',
           ],
    'using/windows': ['windowssidebar.html', 'searchbox.html'],
}

# If true, figures, tables and code-blocks are automatically numbered if they
# has caption. For now, it works only with the HTML builder. Default is False.
numfig = True
# A dictionary mapping 'figure', 'table' and 'code-block' to strings that are
# used for format of figure numbers. Default is to use 'Fig. %s' for 'figure',
# 'Table %s' for 'table' and 'Listing %s' for 'code-block'.
numfig_format = {"figure": u"Рис. %s",
                 "table": u"Таблица %s",
                 "code-block": u"Код %s"}


# If true, figures, tables and code-blocks are automatically numbered if they
# has caption. For now, it works only with the HTML builder. Default is False.
numfig = True
# A dictionary mapping 'figure', 'table' and 'code-block' to strings that are
# used for format of figure numbers. Default is to use 'Fig. %s' for 'figure',
# 'Table %s' for 'table' and 'Listing %s' for 'code-block'.
numfig_format = {"figure": u"Рис. %s",
                 "table": u"Таблица %s",
                 "code-block": u"Код %s"}

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinxcontrib.fulltoc']

# TODO
if 'NO_METRIKA' in os.environ:
    todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Основы Веб-программирования'
copyright = u'2015, uralbash'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.0'
# The full version, including alpha/beta/rc tags.
release = '0.0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'ru'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%d-%m-%Y'
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'mydefault'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'collapsiblesidebar': True,
    'sidebarbgcolor': '#eee',
    'sidebartextcolor': '#33a',
    'sidebarlinkcolor': '#333',
    'relbarbgcolor': '#666',
    'sidebarbtncolor': '#666',
    'footerbgcolor': '#eee',
    'footertextcolor': '#000',
    # link color
    'linkcolor': 'blue',
    'visitedlinkcolor': 'blue'
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = '-doc'


# -- Options for LaTeX output ---------------------------------------------
ADDITIONAL_PREAMBLE = """
\\setcounter{tocdepth}{3}
"""

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4papper',
    'wrapperclass': 'scrbook',
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt',
    # 'fontpkg': '\\usepackage[sfdefault]{cabin}',
    # Additional stuff for the LaTeX preamble.
    'preamble': ADDITIONAL_PREAMBLE,
    'figure_align': 'ht',  # htbp
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'lectures.tex',
     u'Основы Веб-программирования',
     u'Свинцов Дмитрий', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = _LOGO

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', '-', u'Основы Веб-программирования Documentation',
     u'uralbash', '-', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Основы Веб-программирования'
epub_author = u'uralbash'
epub_publisher = u'uralbash'
epub_copyright = u'2015, uralbash'

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'http://docs.python.org/': None,
    'http://docs.sqlalchemy.org/en/latest/': None,
    'http://docs.pylonsproject.org/projects/colander/en/latest/': None,
    'http://deform.readthedocs.org/en/latest/': None,
    'http://initd.org/psycopg/docs/': None,
}


# TODO: сделать через директиву, типа .. note::
def sourcecode(role, rawtext, text, lineno, inliner,
               options={}, content=[]):
    """
    Example:

        See code there :src:`6.www.sync/2.codding/blog/0.paster`.
    """
    # Base URL mainly used by inliner.rfc_reference, so this is correct:
    SOURCE_URL =\
        'https://github.com/ustu/lectures.www/tree/master/sourcecode/'
    ref = SOURCE_URL + text
    set_classes(options)
    node = docutils.nodes.reference(
        rawtext,
        SOURCE_URL + docutils.utils.unescape(text),
        refuri=ref, **options)
    return [node], []


PYLONS_LINKS = {
    'webob': 'http://docs.webob.org/',
    'colander': 'http://docs.pylonsproject.org/projects/colander/en/latest/',
    'deform': 'http://deform.readthedocs.org/en/latest/',
    'chameleon': 'http://pyramid-chameleon.readthedocs.org/en/latest/',
    'peppercorn':
    'http://docs.pylonsproject.org/projects/peppercorn/en/latest/',
}

DATABASE_LINKS = {
    # NoSQL
    'memcached': 'https://ru.wikipedia.org/wiki/Memcached',
    'redis': 'https://ru.wikipedia.org/wiki/Redis',

    # SQL
    'sqlite': 'http://sqlite.org/',
    'postgres': 'http://postgresql.org',
    'postgresql': 'http://postgresql.org',

    # ORM
    'db-api': 'https://www.python.org/dev/peps/pep-0249/',
    'db-api 2.0': 'https://www.python.org/dev/peps/pep-0249/',
    'sqlalchemy': 'http://sqlalchemy.org/',
}

FRAMEWORK_LINKS = {
    'pyramid': 'http://pylonsproject.org/',
    'pylons':
    'http://docs.pylonsproject.org/projects/pylons-webframework/en/latest/',
    'repoze.bfg': 'http://bfg.repoze.org',
    'zope': 'http://www.zope.org/',
    'flask': 'http://flask.pocoo.org/',
    'turbogears': 'http://www.turbogears.org/',
}

OTHER_LINKS = {
    # Web servers
    'nginx': 'http://nginx.org/',
    'paste': 'http://pythonpaste.org/',

    # Template engine
    'jinja': 'http://jinja.pocoo.org/',
    'jinja2': 'http://jinja.pocoo.org/',
    'mako': 'http://www.makotemplates.org/',

    # Cache and Session
    'beaker': 'https://beaker.readthedocs.org/en/latest/',
}

GLOBAL_LINKS = dict(PYLONS_LINKS.items() + OTHER_LINKS.items() +
                    DATABASE_LINKS.items() + FRAMEWORK_LINKS.items())


def global_link(role, rawtext, text, lineno, inliner,
                options={}, content=[]):
    """
    Example:

        See code there :l:`Nginx`.
    """
    link = GLOBAL_LINKS[text.lower()]
    set_classes(options)
    node = docutils.nodes.reference(
        rawtext, docutils.utils.unescape(text),
        refuri=link, **options)
    return [node], []


def setup(app):
    """Install the plugin.

    :param app: Sphinx application context.
    """
    if 'NO_METRIKA' not in os.environ:
        app.add_javascript('js/metrika.js')
    app.add_javascript('js/jquery.fancybox.js')
    app.add_stylesheet('css/jquery.fancybox.css')
    app.add_stylesheet('css/todo.css')

    # Add roles
    app.add_role('src', sourcecode)
    app.add_role('l', global_link)
