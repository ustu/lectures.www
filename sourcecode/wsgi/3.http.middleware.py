#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

from paste.evalexception.middleware import EvalException
from paste.gzipper import middleware as GzipMiddleware
from paste.pony import PonyMiddleware
from paste.session import SessionMiddleware


def counter_app(environ, start_response):
    # Except error
    if 'error' in environ['PATH_INFO'].lower():
        raise Exception('Detect "error" in URL path')

    # Session
    session = environ['paste.session.factory']()
    if 'count' in session:
        count = session['count']
    else:
        count = 1
    session['count'] = count + 1

    # Generate response
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['You have been here %d times!\n' % count, ]

app = SessionMiddleware(counter_app)
app = GzipMiddleware(app)
app = PonyMiddleware(app)  # go to http://localhost:8000/pony
app = EvalException(app)   # go to http://localhost:8000/Errors

if __name__ == '__main__':
    from paste import reloader
    from paste.httpserver import serve

    reloader.install()
    serve(app, host='0.0.0.0', port=8000)
