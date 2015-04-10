from webob import Request
req = Request.blank('/test?check=a&check=b&name=Bob')

print(req.GET)
print(req.GET['check'])
print(req.GET.getall('check'))
print(req.GET.items())
