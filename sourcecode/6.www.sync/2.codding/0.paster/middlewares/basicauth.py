#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
BasicAuth
"""


class BasicAuth(object):

    def __init__(self, app, users, realm='www'):
        self.app = app
        self.users = users
        self.realm = realm

    def __call__(self, environ, start_response):
        auth = environ.get('HTTP_AUTHORIZATION')
        if not auth:
            return self.auth_required(environ, start_response)
        auth_type, enc_auth_info = auth.split(None, 1)
        assert auth_type.lower() == 'basic'
        auth_info = enc_auth_info.decode('base64')
        username, password = auth_info.split(':', 1)
        if self.users.get(username) != password:
            return self.auth_required(environ, start_response)
        environ['REMOTE_USER'] = username
        return self.app(environ, start_response)

    def auth_required(self, environ, start_response):
        status = '401 Authorization Required'
        headers = [('content-type', 'text/plain'),
                   ('WWW-Authenticate',
                    'Basic realm="%s"' % self.realm)]
        start_response(status, headers)
        return ['authentication required']
