#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
FastCGI example
http://flask.pocoo.org/docs/deploying/fastcgi/
http://docs.python.org/2/howto/webservers.html#setting-up-fastcgi
"""
from flup.server.fcgi import WSGIServer


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    yield '<h1>FastCGI Environment</h1>'
    yield '<table>'
    for k, v in sorted(environ.items()):
        yield '<tr><th>%s</th><td>%s</td></tr>' % (k, v)
    yield '</table>'

WSGIServer(app).run()
