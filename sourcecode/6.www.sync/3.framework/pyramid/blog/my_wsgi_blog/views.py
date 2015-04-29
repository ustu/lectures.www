# -*- coding: utf-8 -*-
import deform
from jinja2 import Environment, FileSystemLoader
from webob import Request, Response

from common import get_csrf_token, get_session
from models import Session, Articles


env = Environment(loader=FileSystemLoader('my_wsgi_blog/templates'))


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
        dbsession = Session()
        self.article = dbsession.query(Articles).filter_by(id=article_id).one()
        dbsession.close()


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
        dbsession = Session()
        articles = dbsession.query(Articles).all()
        self.paged_articles = Page(
            articles,
            page=self.page,
            items_per_page=8,
        )
        dbsession.close()

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
            article = Articles(**{'title': self.request.POST['title'],
                                  'content': self.request.POST['content']
                                  })
            dbsession = Session()
            dbsession.add(article)
            dbsession.commit()
            dbsession.close()
            self.session = get_session(self.request).pop('csrf')
            return Response(status=302, location='/blog/')
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
            self.article.title = self.request.POST['title']
            self.article.content = self.request.POST['content']
            dbsession = Session()
            dbsession.add(self.article)
            dbsession.commit()
            dbsession.close()
            self.session = get_session(self.request).pop('csrf')
            return Response(status=302, location='/blog/')
        return Response(
            env.get_template('create.html')
            .render(form=self.get_form().render(
                self.article.__dict__)))


@wsgify
class BlogDelete(BaseArticle):

    def response(self):
        dbsession = Session()
        dbsession.delete(self.article)
        dbsession.commit()
        dbsession.close()
        return Response(status=302, location='/blog/')
