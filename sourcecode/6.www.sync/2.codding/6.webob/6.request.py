from webob import Request
req = Request.blank('/test')

# Set Cookie
req.headers['Cookie'] = 'session_id=9999999;foo=abcdef;bar=2'

print(req.cookies)
print(req.cookies['foo'])
