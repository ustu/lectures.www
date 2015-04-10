from jinja2 import Environment, FileSystemLoader
from webob import Request, Response

from models import ARTICLES

env = Environment(loader=FileSystemLoader('templates'))


def wsgify(view):
    def wrapped(environ, start_response):
        request = Request(environ)
        app = view(request).response()
        return app(environ, start_response)
    return wrapped


class BaseArticle(object):

    def __init__(self, request):
        self.request = request
        article_id = self.request.environ['wsgiorg.routing_args'][1]['id']
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
        return Response(env.get_template('index.html')
                        .render(articles=self.paged_articles))


@wsgify
class BlogCreate(object):

    def __init__(self, request):
        self.request = request

    def response(self):
        if self.request.method == 'POST':
            max_id = max([art['id'] for art in ARTICLES])
            ARTICLES.append(
                {'id': max_id+1,
                 'title': self.request.POST['title'],
                 'content': self.request.POST['content']
                 }
            )
            return Response(status=302, location='/')
        return Response(env.get_template('create.html').render(article=None))


@wsgify
class BlogRead(BaseArticle):

    def response(self):
        if not self.article:
            return Response(status=404)
        return Response(env.get_template('read.html')
                        .render(article=self.article))


@wsgify
class BlogUpdate(BaseArticle):

    def response(self):
        if self.request.method == 'POST':
            self.article['title'] = self.request.POST['title']
            self.article['content'] = self.request.POST['content']
            return Response(status=302, location='/')
        return Response(env.get_template('create.html')
                        .render(article=self.article))


@wsgify
class BlogDelete(BaseArticle):

    def response(self):
        ARTICLES.pop(self.index)
        return Response(status=302, location='/')
