# -*- coding: utf-8 -*-

import sys
import os
# import sphinx_bootstrap_theme
import guzzle_sphinx_theme
# import foundation_sphinx_theme
from recommonmark.parser import CommonMarkParser

# This is the Sphinx config file.
# @see http://www.sphinx-doc.org/en/stable/config.html

project = u'Rackspace DevOps'
copyright = u'2016, Rackspace Ltd.'
author = u'Rackspace'

version = '1.0'
release = '1.0'

sys.path.insert(0, os.path.abspath('_ext'))
# sys.path[0:0] = [os.path.abspath('_themes/foundation-sphinx-theme')]

source_parsers = {
    '.md': CommonMarkParser,
}

extensions = [

    # @see https://github.com/westurner/sphinxcontrib-srclinks
    # 'sphinxcontrib.srclinks',

    # @see https://github.com/peterhudec/foundation-sphinx-theme
    # Does NOT play well with the JSON builder
    # 'foundation_sphinx_theme',

    # @see https://github.com/dreamhost/sphinxcontrib-fulltoc
    # 'sphinxcontrib.fulltoc',

    # @see https://github.com/sbrunner/sphinx-prompt
    'sphinx-prompt',

    # @see https://github.com/OddBloke/sphinx-git
    'sphinx_git',

    # @see https://pypi.python.org/pypi/sphinxcontrib-issuetracker
    'sphinxcontrib.issuetracker',

    # @see https://gist.github.com/mgedmin/6052926
    # 'edit_on_github',
    'rst2pdf.pdfbuilder',

    # 'sphinxcontrib.restbuilder',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    # 'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.exceltable',
    # 'sphinxcontrib.googleanalytics',
    'sphinxcontrib.googlechart',
    'sphinxcontrib.googlemaps',
    # 'sphinxcontrib.libreoffice',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.packetdiag',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.rackdiag',
    'sphinxcontrib.seqdiag',
]

source_suffix = ['.rst', '.md']
source_encoding = 'utf8'

master_doc = 'index'

pygments_style = 'sphinx'

templates_path = ['_templates']
html_static_path = ['_static']

show_authors = True

todo_include_todos = True

# # srclink config; see @https://pypi.python.org/pypi/sphinxcontrib-srclinks
# srclink_project = 'http://github.rackspace.com/devops-ps-uk/devops-ps-creation/'
# srclink_src_path = 'docs/'
# srclink_branch = 'master'
# history_srclink_url = False
# annotate_srclink_url = False
# srclink_src_url = False

# Theme options

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {
#     '**': [
#         # 'globaltoc.html',
#         'localtoc.html',
#         # 'relations.html',
#         'searchbox.html',
#         # 'srclinks.html',
#     ],
#     'index': [
#         # 'globaltoc.html',
#         # 'relations.html',
#         # 'searchbox.html',
#         # 'srclinks.html',
#     ],
# }

html_favicon = 'images/favicon.ico'

# @see https://github.com/peterhudec/foundation-sphinx-theme
# html_theme = 'foundation_sphinx_theme'
# html_theme_path = foundation_sphinx_theme.HTML_THEME_PATH

# @see http://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html
# html_theme = 'bootstrap'
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# html_theme = 'bizstyle'

# Adds an HTML table visitor to apply Bootstrap table classes
html_translator_class = 'guzzle_sphinx_theme.HTMLTranslator'
html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Register the theme as an extension to generate a sitemap.xml
# extensions.append("guzzle_sphinx_theme")

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {

#### For Guzzle theme
    # Set the name of the project to appear in the sidebar
    "project_nav_name": project,


#### For bootstrap theme
    # # Global TOC depth for "site" navbar tab. (Default: 1)
    # # Switching to -1 shows all levels.
    # 'globaltoc_depth': 2,
    #
    # # HTML navbar class (Default: "navbar") to attach to <div> element.
    # # For black navbar, do "navbar navbar-inverse"
    # 'navbar_class': "navbar navbar-inverse",
    #
    # # Render the next and previous page links in navbar. (Default: true)
    # 'navbar_sidebarrel': False,
    #
    # # Render the current pages TOC in the navbar. (Default: true)
    # 'navbar_pagenav': True,
    #
    # # Bootswatch (http://bootswatch.com/) theme.
    # # Options are nothing (default) or the name of a valid theme
    # # such as "amelia" or "cosmo".
    # 'bootswatch_theme': "flatly",
    #
    # # Location of link to source.
    # # Options are "nav" (default), "footer" or anything else to exclude.
    # 'source_link_position': "footer",

#### For Foundation theme
    # # Use this if the top-level items of the toctree don't fit in the top-bar navigation.
    # # If True, the whole toctree will be placed inside a single top-level item.
    # 'top_bar_force_fit': True,
    #
    # # The title of the aformentioned top-level item. Default is "Sections"
    # 'top_bar_content_title': 'Contents',
    #
    # # If true a bar with Facebook, Google+ and Twitter social buttons will be displayed
    # # underneath the header.
    # 'social_buttons': False,
    #
    # # If set, Google Analytics code will be appended to body of each page.
    # 'google_analytics_id': 'your-google-analytics-id',
}

# html_theme = 'rackspace-canon'
# html_theme_path = ['./_themes']

# ReST builder options
# @see https://pythonhosted.org/sphinxcontrib-restbuilder/
rst_file_suffix = '.rst'
rst_link_suffix = ''
rst_line_width = 78
rst_indent = 4
# def rst_file_transform(docname):
#     if docname == 'index':
#         docname = 'home'
#     return docname.title() + rst_file_suffix
# def rst_link_transform(docname):
#     if docname == 'index':
#         return 'wiki'
#     return 'wiki/' + docname.title()

# PDF options
## @see http://rst2pdf.ralsina.me/handbook.html#sphinx
pdf_documents = [
    # ('index', u'full', u'DevOps Professional Services', u'Rackspace UK'),
    # master document, name of the generated pdf, title of the pdf, author name in the pdf
    (
        'solution_design/index',
        u'solution-design',
        u'Rackspace DevOps',
        u'Rackspace UK'
    ),
]

# A comma-separated list of custom stylesheets. Example:
# pdf_stylesheets = ['sphinx', 'kerning', 'serif', 'a4']
pdf_stylesheets = ['sphinx', 'kerning', 'serif', 'a4', 'rst2pdf-styles.txt']
# pdf_stylesheets = ['rst2pdf-styles.txt']

pdf_style_path = ['./docs/_themes/']

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
pdf_break_level = 0

# Show Table Of Contents at the beginning?
pdf_use_toc = False

# If false, no coverpage is generated.
pdf_use_coverpage = False

# Support the ..raw:: html directive
pdf_raw_html = True
