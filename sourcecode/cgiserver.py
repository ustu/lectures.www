#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Demo CGI Server
"""
import BaseHTTPServer
import CGIHTTPServer
import cgitb

cgitb.enable()  # This line enables CGI error reporting

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/cgi-bin"]

httpd = server(server_address, handler)
httpd.serve_forever()
