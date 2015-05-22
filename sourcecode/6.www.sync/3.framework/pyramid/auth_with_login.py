from wsgiref.simple_server import make_server

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.security import Allow, forget, remember


class HelloFactory(object):
    def __init__(self, request):
        self.__acl__ = [
            (Allow, 'vasya', 'view'),
            (Allow, 'group:editors', 'add'),
            (Allow, 'group:editors', 'edit'),
        ]


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


def login(request):
    headers = remember(request, 'vasya')
    return HTTPFound(location=request.route_url('hello', name='vasya'),
                     headers=headers)


def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('hello', name='log out!!!'),
                     headers=headers)


if __name__ == '__main__':
    authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(root_factory=HelloFactory)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world,
                    route_name='hello',
                    permission='view')

    # login form
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_view(login, route_name='login')
    config.add_view(logout, route_name='logout')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
