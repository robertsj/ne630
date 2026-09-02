#!/usr/bin/env python3

extensions = [
    "sphinx.ext.githubpages",
]

source_suffix = {".rst": "restructuredtext"}
root_doc = "index"

project = "NE 630: Nuclear Reactor Theory"
copyright = "2026, Jeremy Roberts"
author = "Jeremy Roberts"
release = "Fall 2026"

exclude_patterns = ["_build", "README.md", "Thumbs.db", ".DS_Store"]
templates_path = ["_templates"]

html_theme = "alabaster"
html_title = "NE 630: Nuclear Reactor Theory"
html_static_path = ["_static"]
html_copy_source = False
html_show_sourcelink = False
html_theme_options = {
    "description": "Nuclear Reactor Theory handouts and course materials",
    "fixed_sidebar": False,
}
