from webob import Request
req = Request.blank('/blog?page=4')

print(req.method)
print(req.scheme)
print(req.path_info)
print(req.host)
print(req.host_url)
print(req.application_url)
print(req.path_url)
print(req.url)
print(req.path)
print(req.path_qs)
print(req.query_string)
