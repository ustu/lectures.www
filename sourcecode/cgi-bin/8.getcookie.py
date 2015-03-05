#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

# Import modules for CGI handling
from os import environ

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Get Cookie</title>")
print("</head>")
print("<body>")

if 'HTTP_COOKIE' in environ:
    for cookie in environ['HTTP_COOKIE'].split(';'):
        (key, value) = cookie.split('=')
        print("%s: %s" % (key, value))
        print("<br/>")

print("</body>")
print("</html>")
