from beaker.middleware import SessionMiddleware


def simple_app(environ, start_response):
    # Get the session object from the environ
    session = environ['beaker.session']

    # Set some other session variable
    session['counter'] = session.get('counter', 0) + 1
    session.save()

    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['Counter value is: %s' % session['counter']]

# Configure the SessionMiddleware
session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': True,
}
wsgi_app = SessionMiddleware(simple_app, session_opts)


if __name__ == '__main__':
    from paste.httpserver import serve

    serve(wsgi_app, host='0.0.0.0', port=8000)
