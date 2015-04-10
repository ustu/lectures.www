from webob import Request
req = Request.blank('/test')

print(req.POST)  # empty
print(req.POST.items())
print

# Set POST
req.method = 'POST'
req.body = 'name=Vasya&email=vasya@example.com'

print(req.POST)  # not empty
print(req.POST['name'])
print(req.POST['email'])
