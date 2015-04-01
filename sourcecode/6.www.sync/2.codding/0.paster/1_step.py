#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Simple blog
"""
from middlewares.urldispatch import URLDispatch


def blog(environ, start_response):
    # Generate response
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Simple Blog', ]

# URL dispatching middleware
app_list = [
    ('/', blog),
]
dispatch = URLDispatch(app_list)

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(dispatch, host='0.0.0.0', port=8000)
