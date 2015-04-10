from webob import Request
req = Request.blank('/blog?page=4')

from pprint import pprint
pprint(req.environ)
