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

import urlrelay
from views import BlogCreate, BlogDelete, BlogRead, BlogUpdate


def authfunc(environ, username, password):
    return username == 'admin' and password == '123'


def make_wsgi_app():
    # BasicAuth applications
    create = AuthBasicHandler(BlogCreate, 'www', authfunc)
    update = AuthBasicHandler(BlogUpdate, 'www', authfunc)
    delete = AuthBasicHandler(BlogDelete, 'www', authfunc)

    # URL dispatching middleware
    urlrelay.register('^/$', 'views.BlogIndex')
    urlrelay.register('^/article/add$', create)
    urlrelay.register('^/article/(?P<id>\d+)$', BlogRead)
    urlrelay.register('^/article/(?P<id>\d+)/edit$', update)
    urlrelay.register('^/article/(?P<id>\d+)/delete$', delete)
    dispatch = urlrelay.URLRelay()
    return dispatch

if __name__ == '__main__':
    from paste.httpserver import serve
    app = make_wsgi_app()
    serve(app, host='0.0.0.0', port=8000)
