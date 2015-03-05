#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
#
# CGI checkbox
# http://www.tutorialspoint.com/python/python_cgi_programming.htm

import cgi

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
maths = form.getvalue('maths')
physics = form.getvalue('physics')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Checkbox - Third CGI Program</title>")
print("</head>")
print("<body>")

if maths:
    print("Maths Flag: ON")
else:
    print("Maths Flag: OFF")

print("<br>")

if physics:
    print("Physics Flag: ON")
else:
    print("Physics Flag: OFF")

print("</body>")
print("</html>")
