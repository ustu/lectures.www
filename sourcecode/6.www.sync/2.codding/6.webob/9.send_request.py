from webob import Request

req = Request.blank('http://en.wikipedia.org/wiki/HTTP')

from pprint import pprint
pprint(req)
print
print(req.get_response())
