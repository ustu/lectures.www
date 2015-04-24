import deform
from jinja2 import Environment, FileSystemLoader
from webob import Request, Response

from common import get_csrf_token, get_session
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


class BaseArticleForm(object):

    def get_form(self):
        from forms import CreateArticle
        self.session = get_session(self.request)
        self.session['csrf'] = get_csrf_token(self.session)
        schema = CreateArticle().bind(request=self.request)
        submit = deform.Button(name='submit',
                               css_class='blog-form__button')
        self.form = deform.Form(schema, buttons=(submit,))
        return self.form


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
class BlogCreate(BaseArticleForm):

    def __init__(self, request):
        self.request = request

    def response(self):
        if self.request.method == 'POST':
            submitted = self.request.POST.items()
            try:
                self.get_form().validate(submitted)
            except deform.ValidationFailure as e:
                return Response(
                    env.get_template('create.html').render(form=e.render()))
            max_id = max([art['id'] for art in ARTICLES])
            ARTICLES.append(
                {'id': max_id+1,
                 'title': self.request.POST['title'],
                 'content': self.request.POST['content']
                 }
            )
            self.session = get_session(self.request).pop('csrf')
            return Response(status=302, location='/')
        return Response(env.get_template('create.html')
                        .render(form=self.get_form().render()))


@wsgify
class BlogRead(BaseArticle):

    def response(self):
        if not self.article:
            return Response(status=404)
        return Response(env.get_template('read.html')
                        .render(article=self.article))


@wsgify
class BlogUpdate(BaseArticle, BaseArticleForm):

    def response(self):
        if self.request.method == 'POST':
            submitted = self.request.POST.items()
            try:
                self.get_form().validate(submitted)
            except deform.ValidationFailure as e:
                return Response(
                    env.get_template('create.html').render(form=e.render()))
            self.article['title'] = self.request.POST['title']
            self.article['content'] = self.request.POST['content']
            self.session = get_session(self.request).pop('csrf')
            return Response(status=302, location='/')
        return Response(
            env.get_template('create.html')
            .render(form=self.get_form().render(self.article)))


@wsgify
class BlogDelete(BaseArticle):

    def response(self):
        ARTICLES.pop(self.index)
        return Response(status=302, location='/')
