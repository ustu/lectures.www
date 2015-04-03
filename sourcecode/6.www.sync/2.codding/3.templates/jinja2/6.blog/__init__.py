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
from paste.auth.basic import AuthBasicHandler

import selector
from views import BlogCreate, BlogDelete, BlogIndex, BlogRead, BlogUpdate


def authfunc(environ, username, password):
    return username == 'admin' and password == '123'


def make_wsgi_app():
    # BasicAuth applications
    create = AuthBasicHandler(BlogCreate, 'www', authfunc)
    update = AuthBasicHandler(BlogUpdate, 'www', authfunc)
    delete = AuthBasicHandler(BlogDelete, 'www', authfunc)

    # URL dispatching middleware
    dispatch = selector.Selector()
    dispatch.add('/', GET=BlogIndex)
    dispatch.prefix = '/article'
    dispatch.add('/add', GET=create, POST=create)
    dispatch.add('/{id:digits}', GET=BlogRead)
    dispatch.add('/{id:digits}/edit', GET=update, POST=update)
    dispatch.add('/{id:digits}/delete', GET=delete)
    return dispatch

if __name__ == '__main__':
    from paste.httpserver import serve
    app = make_wsgi_app()
    serve(app, host='0.0.0.0', port=8000)
