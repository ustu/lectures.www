#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

# standard library
import os
import sys

sys.path.insert(0, os.path.abspath('../_lectures/docs/'))

from config_sphinx import *  # noqa isort:skip

project = u'Основы Веб-программирования'
html_title = project
epub_title = project

edit_on_github_project = 'ustu/lectures.www'
edit_on_github_branch = 'master'

# for Sitemap
set_base_url("https://lectureswww.readthedocs.io/")  # noqa
html_extra_path = ["html_extra_path"]

latex_documents = [
    (
        'index',
        'lectures.tex',
        project,
        u'Свинцов Дмитрий',
        'manual'
    ),
]

my_intersphinx = {
    # Pylons
    'http://pyramid-tm.readthedocs.io/en/latest/': None,
    'http://docs.pylonsproject.org/projects/colander/en/latest/': None,
    'http://docs.pylonsproject.org/projects/pyramid/en/latest/': None,
    'http://docs.pylonsproject.org/projects/pyramid-debugtoolbar/en/latest/':
    None,
    'http://deform.readthedocs.io/en/latest/': None,
    'http://venusian.readthedocs.io/en/latest/': None,
    'http://pyramid-sqlalchemy.readthedocs.io/en/latest/': None,
    'http://docs.webob.org/en/stable/': None,
    'http://paste.readthedocs.io/en/latest/': None,
    'http://jinja.pocoo.org/docs/dev/': None,
}

intersphinx_mapping = dict(
    list(intersphinx_mapping.items())  # noqa
    + list(my_intersphinx.items())
)

exclude_patterns += [  # noqa
    '999.additions/index.rst'
]
