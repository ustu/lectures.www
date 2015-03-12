#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Example from pep-3333
"""
from server import run_with_cgi


def simple_app(environ, start_response):
    """ Simple WSGI application"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    yield 'Hello, World!'


class AppClass:

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

        self.HTML_START = b"""<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
            "http://www.w3.org/TR/html4/strict.dtd">
        <html lang="en">
          <head>
            <meta http-equiv="content-type" content="text/html; charset=utf-8">
            <title>title</title>
            <link rel="stylesheet" type="text/css" href="style.css">
            <script type="text/javascript" src="script.js"></script>
          </head>
          <body>
        """
        self.HELLO_WORLD = b"Hello world!\n"
        self.HTML_END = b"""
          </body>
        </html>
        """

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        yield self.HTML_START
        yield b'<h1>PEP-3333</h1>'
        yield b'<ul>'
        for value in self.environ.items():
            env = '<li><b>{0}</b>: {1}</li>'.format(*value)
            yield env.encode('utf-8')
        yield b'</ul>'
        yield b'<br/>'
        yield b'<br/>'
        yield self.HELLO_WORLD
        yield self.HTML_END

if __name__ == '__main__':
    run_with_cgi(AppClass)
