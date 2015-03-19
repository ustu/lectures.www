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


def blog(environ, start_response):
    # Generate response
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Simple Blog', ]

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(blog, host='0.0.0.0', port=8000)
