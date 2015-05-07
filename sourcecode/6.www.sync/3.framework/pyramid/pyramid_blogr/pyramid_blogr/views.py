import deform
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config
from pyramid_sqlalchemy import Session

from .forms import get_form
from .models import Article


@view_config(route_name='blog',
             renderer='blog/index.jinja2')
def index_page(request):
    page = int(request.params.get('page', 1))
    paginator = Article.get_paginator(request, page)
    return {'paginator': paginator}


@view_config(route_name='blog_article', renderer='blog/read.jinja2')
def blog_view(request):
    id = int(request.matchdict.get('id', -1))
    article = Article.by_id(id)
    if not article:
        return HTTPNotFound()
    return {'article': article}


@view_config(route_name='blog_create',
             renderer='blog/edit.jinja2')
@view_config(route_name='blog_action', match_param='action=edit',
             renderer='blog/edit.jinja2')
def blog_create(request):
    form = get_form(request)
    if request.method == 'POST':
        try:
            values = form.validate(request.POST.items())
        except deform.ValidationFailure as e:
            return {'form': e.render(),
                    'action': request.matchdict.get('action')}
        if request.matchdict.get('action', '') == 'edit':
            article = Session.query(Article)\
                .filter_by(id=request.matchdict['id']).one()
            article.title = request.POST['title']
            article.content = request.POST['content']
        else:
            article = Article(**values)
        Session.add(article)
        return HTTPFound(location=request.route_url('blog'))
    values = {}
    if request.matchdict.get('action', '') == 'edit':
        values = Session.query(Article)\
            .filter_by(id=request.matchdict['id']).one().__dict__
    return {'form': form.render(values),
            'action': request.matchdict.get('action')}


@view_config(route_name='blog_action', match_param='action=delete')
def blog_delete(request):
    article = Session.query(Article)\
        .filter_by(id=request.matchdict['id']).one()
    Session.delete(article)
    return HTTPFound(location=request.route_url('blog'))


@view_config(route_name='auth', match_param='action=in', renderer='string',
             request_method='POST')
@view_config(route_name='auth', match_param='action=out', renderer='string')
def sign_in_out(request):
    return {}
