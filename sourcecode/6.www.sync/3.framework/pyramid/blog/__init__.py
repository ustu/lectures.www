from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello(request):
    return Response('Hello world! See you blog <a href="blog/">there</a>!')


from pyramid.wsgi import wsgiapp


@wsgiapp
def hello_world(environ, start_response):
    body = 'Hello world'
    start_response('200 OK', [('Content-Type', 'text/plain'),
                              ('Content-Length', str(len(body)))])
    return [body]

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello_world', '/')
    config.add_route('hello_world_wsgi', '/hello_wsgi')
    config.add_view(hello, route_name='hello_world')
    config.add_view(hello_world, route_name='hello_world_wsgi')

    from my_wsgi_blog import make_wsgi_app
    blog_app = make_wsgi_app()
    from paste import urlmap
    mapping = urlmap.URLMap()
    mapping['/blog'] = blog_app

    from paste.cascade import Cascade
    pyramid_app = config.make_wsgi_app()
    app = Cascade([mapping, pyramid_app])

    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
