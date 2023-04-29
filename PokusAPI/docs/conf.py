"""Sphinx configuration."""
project = "pokusapi"
author = "Claudio Jolowicz"
copyright = "2023, Claudio Jolowicz"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
