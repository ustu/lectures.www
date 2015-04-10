environ = {
    'HTTP_HOST': 'localhost:80',
    'PATH_INFO': '/article',
    'QUERY_STRING': 'id=1',
    'REQUEST_METHOD': 'GET',
    'SCRIPT_NAME': ''
}

from webob import Request
req = Request(environ)

from pprint import pprint
pprint(req.environ)
