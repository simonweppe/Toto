# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import os,sys
sys.path.append('.')
from links.link import *
from links import *
#sys.path.insert(0, os.path.abspath('../Toto'))
import scipy
import toto


project = 'Toto'
copyright = '2021, Calypso Science'
author = 'Calypso Science'

# The full version, including alpha/beta/rc tags
release = toto.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "nbsphinx",
    "sphinx_gallery.gen_gallery"
]

sphinx_gallery_conf = {
     'examples_dirs': '../examples/',   # path to your example scripts
     'gallery_dirs': './gallery',  # path to where to save gallery generated output,
     # #'filename_pattern': '/example_(?!long_)',
     # 'backreferences_dir': None,
     # 'capture_repr': ('_repr_html_', '__repr__'),
     # 'abort_on_example_error': False,
     # 'thumbnail_size': (300, 300)
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']