#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

import os
import sys

sys.path.insert(0, os.path.abspath('../_lectures/docs/'))

from config_sphinx import *  # noqa

project = u'Основы Веб-программирования'
epub_title = project
latex_documents = [
    ('index', 'lectures.tex',
     project,
     u'Свинцов Дмитрий', 'manual'),
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
}
intersphinx_mapping = dict(
    list(intersphinx_mapping.items())
    + list(my_intersphinx.items())
)
