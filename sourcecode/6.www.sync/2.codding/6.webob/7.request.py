from webob import Request


def wsgi_app(environ, start_response):
    request = Request(environ)
    if request.path == '/test':
        start_response('200 OK', [('Content-type', 'text/plain')])
        return ['Hi!']
    start_response('404 Not Found', [('Content-type', 'text/plain')])

req = Request.blank('/test')
status, headers, app_iter = req.call_application(wsgi_app)
print(status)
print(headers)
print(app_iter)
print

req = Request.blank('/bar')
status, headers, app_iter = req.call_application(wsgi_app)
print(status)
print(headers)
print(app_iter)
