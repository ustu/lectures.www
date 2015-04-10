from webob import Request, Response


def wsgi_app(environ, start_response):
    response = Response()
    response.content_type = 'text/plain'

    parts = []
    for name, value in sorted(environ.items()):
        parts.append('%s: %r' % (name, value))
    response.body = '\n'.join(parts)
    return response(environ, start_response)

req = Request.blank('/test')
print(req.call_application(wsgi_app))  # WSGI-application response
print
print(req.get_response(wsgi_app))  # HTTP response
