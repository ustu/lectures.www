from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_sqlalchemy')
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path('pyramid_blogr:templates')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('blog', '/')
    config.add_route('blog_article', '/article/{id:\d+}/{slug}')
    config.add_route('blog_action', '/{action}')
    config.add_route('auth', '/sign/{action}')

    config.scan()
    return config.make_wsgi_app()
