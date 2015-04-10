from jinja2 import Environment, FileSystemLoader

from models import ARTICLES

env = Environment(loader=FileSystemLoader('templates'))


class BaseBlog(object):

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response


def wsgify(view):
    from webob import Request

    def wrapped(environ, start_response):
        request = Request(environ)
        app = view(request).response()
        return app(environ, start_response)
    return wrapped


class BaseArticle(BaseBlog):

    def __init__(self, *args):
        super(BaseArticle, self).__init__(*args)
        article_id = self.environ['wsgiorg.routing_args'][1]['id']
        (self.index,
         self.article) = next(((i, art) for i, art in enumerate(ARTICLES)
                               if art['id'] == int(article_id)),
                              (None, None))


@wsgify
class BlogIndex(object):

    def __init__(self, request):
        self.page = request.GET.get('page', '1')
        from paginate import Page
        self.paged_articles = Page(
            ARTICLES,
            page=self.page,
            items_per_page=8,
        )

    def response(self):
        from webob import Response
        return Response(env.get_template('index.html')
                        .render(articles=self.paged_articles)
                        .encode('utf-8'))


class BlogCreate(BaseBlog):

    def __iter__(self):
        if self.environ['REQUEST_METHOD'].upper() == 'POST':
            from urlparse import parse_qs
            values = parse_qs(self.environ['wsgi.input'].read())
            max_id = max([art['id'] for art in ARTICLES])
            ARTICLES.append(
                {'id': max_id+1,
                 'title': values['title'].pop().decode('utf-8'),
                 'content': values['content'].pop().decode('utf-8')
                 }
            )
            self.start('302 Found',
                       [('Content-Type', 'text/html'),
                        ('Location', '/')])
            return

        self.start('200 OK', [('Content-Type', 'text/html')])
        yield env.get_template('create.html').render(article=None)


class BlogRead(BaseArticle):

    def __iter__(self):
        if not self.article:
            self.start('404 Not Found', [('content-type', 'text/plain')])
            yield 'not found'
            return

        self.start('200 OK', [('Content-Type', 'text/html')])
        yield env.get_template('read.html').render(article=self.article)\
            .encode('utf-8')


class BlogUpdate(BaseArticle):

    def __iter__(self):
        if self.environ['REQUEST_METHOD'].upper() == 'POST':
            from urlparse import parse_qs
            values = parse_qs(self.environ['wsgi.input'].read())
            self.article['title'] = values['title'].pop().decode('utf-8')
            self.article['content'] = values['content'].pop().decode('utf-8')
            self.start('302 Found',
                       [('Content-Type', 'text/html'),
                        ('Location', '/')])
            return
        self.start('200 OK', [('Content-Type', 'text/html')])
        yield env.get_template('create.html').render(article=self.article)\
            .encode('utf-8')


class BlogDelete(BaseArticle):

    def __iter__(self):
        self.start('302 Found',  # '301 Moved Permanently',
                   [('Content-Type', 'text/html'),
                    ('Location', '/')])
        ARTICLES.pop(self.index)
        yield ''
